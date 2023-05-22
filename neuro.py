import argparse
from math import pow, ceil
import os
import random
import urllib.request
import pathlib
import numpy
import pandas as pd
import cv2
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from keras.layers import Dropout, BatchNormalization
from keras.models import Sequential
from sklearn import model_selection
from keras.models import load_model

def csv_file_writer(data, name):
    df = pd.DataFrame(data)
    df.to_csv(f'{name}.csv', header = False, sep = ' ', index = False)
        
ell_ra_dec = []
edge_ra_dec = []
acw_ra_dec = []
cw_ra_dec = []

with open('GalaxyZoo1_DR_table2.csv', 'r') as data:
    for st in data:
        vals = st.split(',')
        RA = vals[1].split(':')
        DEC = vals[2].split(':')
        if vals[4] != 'P_EL' and float(vals[4]) > 0.8:    
            ell_ra_dec.append(['nearest:B', RA[0], RA[1], RA[2], DEC[0], DEC[1], DEC[2]])    
        if vals[5] != 'P_CW' and float(vals[5]) > 0.8:    
            cw_ra_dec.append(['nearest:B',RA[0], RA[1], RA[2], DEC[0], DEC[1], DEC[2]])    
        if vals[6] != 'P_ACW' and float(vals[6]) > 0.8:    
            acw_ra_dec.append(['nearest:B',RA[0], RA[1], RA[2], DEC[0], DEC[1], DEC[2]])    
        if vals[7] != 'P_EDGE' and float(vals[7]) > 0.8:    
            edge_ra_dec.append(['nearest:B',RA[0], RA[1], RA[2], DEC[0], DEC[1], DEC[2]])    
              

#csv_file_writer(ell_ra_dec, 'EL')
#csv_file_writer(cw_ra_dec, 'CW')
#csv_file_writer(acw_ra_dec, 'ACW')
#csv_file_writer(edge_ra_dec, 'EDGE')

def analyses_galaxies(file_name):
    with open(file_name + '.txt', 'r') as data_inp:
        with open(file_name + 'set.txt', 'w') as data_out:
            for st in data_inp:
                if st.startswith('nearest'):
                    vals = st.split('|')
                    if not  vals[2].isspace():
                        d = pow(10, float(vals[2])) * 6
                        if d > 15:
                            RA_DEC = vals[0].split()
                            data_out.write(f'{RA_DEC[1]} {RA_DEC[2]} {RA_DEC[3]} {RA_DEC[4]} {RA_DEC[5]} {RA_DEC[6]} {vals[1]} {d}\n')

#analyses_galaxies('uploaderEL')
#analyses_galaxies('uploaderEDGE')
#analyses_galaxies('uploaderCW')
#analyses_galaxies('uploaderACW')

def image_download(file_name, galaxy_type):
    if not os.path.exists(galaxy_type):
        os.makedirs(galaxy_type)
    scale = 0.396127
    with open(file_name, 'r') as data_inp:
        numb = 0
        for st in data_inp:
            if not os.path.exists(galaxy_type + '/'+ str(numb) +'.jpg'):
                vals = st.split()
                RA = f'{vals[0]}:{vals[1]}:{vals[2]}'    
                DEC = f'{vals[3]}:{vals[4]}:{vals[5]}'  
                d = float(vals[7])
                size = ceil(1.5 * d / scale)                           
                url = f'https://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg?TaskName=Skyserver.Explore.Image&ra={RA}&dec={DEC}&scale={scale}&width={size}&height={size}.'
                print(url)
                try:
                    urllib.request.urlretrieve(url, galaxy_type + '/'+ str(numb) +'.jpg')
                except urllib.error.HTTPError as ex:
                    print(ex)
            numb += 1

#image_download('uploaderELset.txt', 'elliptical')
#image_download('uploaderEDGEset.txt', 'edge')

#image_download('uploaderACWset.txt', 'spiral')
#image_download('uploaderCWset.txt', 'spiral')

def make_model():
    model = Sequential()
    model.add(Conv2D(4, kernel_size=3, activation='relu',input_shape=(64, 64, 3)))
    model.add(Conv2D(4, kernel_size=3, activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid',data_format=None))
    model.add(Dropout(rate=0.3))
    model.add(Conv2D(8, kernel_size=3, activation='relu', input_shape=(64, 64, 3)))
    model.add(Conv2D(8, kernel_size=3, activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid',data_format=None))
    model.add(Flatten())
    model.add(Dropout(rate=0.3))
    model.add(Dense(50, activation="relu"))
    model.add(Dense(3, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])
    return model        

def make_dataset():
    elliptical_galaxies = []
    spiral_galaxies = []
    edge_galaxies = []
    for f in pathlib.Path("elliptical").glob("*.jpg"):
        file_name = str(f)
        elliptical_galaxies.append(cv2.cvtColor(cv2.resize(cv2.imread(file_name), (64, 64)), cv2.COLOR_BGR2RGB))
    for f in pathlib.Path("spiral").glob("*.jpg"):
        file_name = str(f)
        spiral_galaxies.append(cv2.cvtColor(cv2.resize(cv2.imread(file_name), (64, 64)), cv2.COLOR_BGR2RGB))
    for f in pathlib.Path("edge").glob("*.jpg"):
        file_name = str(f)
        edge_galaxies.append(cv2.cvtColor(cv2.resize(cv2.imread(file_name), (64, 64)), cv2.COLOR_BGR2RGB))
    n_ell = len(elliptical_galaxies)
    print(n_ell)
    n_sp = len(spiral_galaxies)
    n_edge = len(edge_galaxies)
    set_size0 = 8 * max(n_ell, n_sp, n_edge, 10000)
    for i in range(n_ell, set_size0):
        m = cv2.getRotationMatrix2D((random.randint(12, 52), random.randint(12, 52)), random.randint(-180, 180), 1)
        elliptical_galaxies.append(cv2.warpAffine(elliptical_galaxies[random.randint(0, n_ell)], m, (64, 64)))
    for i in range(n_sp, set_size0):
        m = cv2.getRotationMatrix2D((random.randint(12, 52), random.randint(12, 52)), random.randint(-180, 180), 1)
        spiral_galaxies.append(cv2.warpAffine(spiral_galaxies[random.randint(0, n_sp)], m, (64, 64)))
    for i in range(n_edge, set_size0):
        m = cv2.getRotationMatrix2D((random.randint(12, 52), random.randint(12, 52)), random.randint(-180, 180), 1)
        edge_galaxies.append(cv2.warpAffine(edge_galaxies[random.randint(0, n_edge)], m, (64, 64)))
    galaxies = elliptical_galaxies + spiral_galaxies + edge_galaxies
    elliptical_galaxies.clear()
    spiral_galaxies.clear()
    edge_galaxies.clear()
    labels = []
    for i in range(set_size0):
        labels.append(numpy.array([1, 0, 0]))
    for i in range(set_size0, 2 * set_size0):
        labels.append(numpy.array([0, 1, 0]))
    for i in range(2 * set_size0, 3 * set_size0):
        labels.append(numpy.array([0, 0, 1]))
    g_array = numpy.array(galaxies)
    galaxies.clear()
    l_array = numpy.array(labels)
    labels.clear()
    return g_array, l_array

def train_model():
    galaxies_array, labels_array = make_dataset()
    data_train, data_test, labels_train, labels_test = model_selection.train_test_split(galaxies_array, labels_array, test_size=0.2)
    model = make_model()
    model.fit(data_train, labels_train, validation_data=(data_test, labels_test), epochs=5, batch_size=32)
    model.save("model_class.h5")

def test_model(file_name, model_name):
    model = load_model(model_name)
    img = cv2.imread(file_name)
    str_results = ["elliptical", "spiral", "edge-on"]
    if img.shape[0] > img.shape[1]:
        center = round(img.shape[1] / 2)
        sz = round(img.shape[0] / 2)
        img = numpy.copy(img[:, (center - sz):(center + sz), :])
    else:
        center = round(img.shape[0] / 2)
        sz = round(img.shape[1] / 2)
        img = numpy.copy(img[(center - sz):(center + sz), :, :])
    img = cv2.cvtColor(cv2.resize(img, (64, 64)), cv2.COLOR_BGR2RGB)
    print(f"{file_name}:")
    res = model.predict(numpy.array([img]))
    print(f"elliptical: {res[0][0]}")
    print(f"spiral: {res[0][1]}")
    print(f"edge-on: {res[0][2]}")
    if max(res[0]) > 0.75:    
        print(f"RESULT: {str_results[numpy.argmax(res)]} galaxy\n")
    else:
        print(f"Not classified") 

#train_model()
test_model('277.jpg','model_class.h5')         
    
