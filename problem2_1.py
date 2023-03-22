from astropy.io import fits
import math
import numpy as np
import matplotlib.pyplot as plt
from photutils import aperture

hdul = fits.open('data.fits')
#print(hdul.info())
n=200
m= math.floor(n/2)
image_data_med = np.ndarray(shape=hdul[1].data.shape, dtype='f4')
np.median([hdul[i+1].data for i in range(m)], axis=0, out=image_data_med)

image_data_mean = np.ndarray(shape=hdul[1].data.shape, dtype='f4')
np.mean([hdul[i+1].data for i in range(m)], axis=0, out=image_data_mean)

X=[i for i in range(1,n+1)]
Ix_1=[]
Ix_2=[]

for i in range(n):
    Ix_1 = np.append(Ix_1, image_data_med[m][i]/2 + image_data_med[m-1][i]/2 )
    Ix_2 = np.append(Ix_2, image_data_mean[m][i]/2 + image_data_mean[m-1][i]/2)

r=[i for i in range(1,n+1)]
fx_1=np.ndarray(shape=n, dtype='f4')
fx_2=np.ndarray(shape=n, dtype='f4')
for i in range(n):    
    apermed = aperture.CircularAperture((m,m), r=r[i])
    apermean= aperture.CircularAperture((m,m), r=r[i])
    fx_1[i]= float(aperture.aperture_photometry(image_data_med, apermed)['aperture_sum'][0])
    fx_2[i]= float(aperture.aperture_photometry(image_data_mean, apermean)['aperture_sum'][0])
    
fig, axs = plt.subplots(2, 2)
axs[0][0].imshow(image_data_med , cmap= 'gray')
axs[1][0].imshow(image_data_mean , cmap= 'gray')
axs[0][0].set_title('Median')
axs[1][0].set_title('Mean')
axs[0][1].plot(X,Ix_1)
axs[1][1].plot(X,Ix_2)
fig.set_size_inches(12, 6)
plt.show()

fig, axs = plt.subplots(2, 2)
axs[0][0].imshow(image_data_med , cmap= 'gray')
axs[1][0].imshow(image_data_mean , cmap= 'gray')
axs[0][0].set_title('Median')
axs[1][0].set_title('Mean')
axs[0][1].plot(r,fx_1)
axs[1][1].plot(r,fx_2)
fig.set_size_inches(12, 6)
plt.show()
