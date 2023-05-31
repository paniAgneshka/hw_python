import numpy as np
import astropy.io.fits as fits
import os
from astropy.modeling import models, fitting
import matplotlib.pyplot as plt
from photutils.detection import find_peaks
from astropy.stats import sigma_clipped_stats
from photutils.aperture import CircularAperture
import scipy
from photutils import detect_threshold, detect_sources

from astropy.convolution import Gaussian2DKernel

image = fits.getdata('data.fits')
mean, median, std = sigma_clipped_stats(image, sigma=6.0)

threshold = median + (5.0 * std)

sigma = 3.0 / (2.0 * np.sqrt(2.0 * np.log(2.0))) # FWHM = 3
kernel = Gaussian2DKernel(sigma, x_size=3, y_size=3)
kernel.normalize()
segm = detect_sources(image, threshold, npixels=5, kernel=kernel)
segm_data = np.zeros((200,200))
for i in range(200):
    for j in range(200):
        if segm.data[i][j] == 1:
            segm_data[i][j] = image[i][j]


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax1.imshow(image, origin='lower', interpolation='nearest')
ax2.imshow(segm.data, origin='lower', interpolation='nearest')
plt.show()
tbl = find_peaks(image, threshold, box_size=5, footprint=np.ones((5, 5)), border_width=5)

plt.imshow(image-segm_data )
plt.show()

tbl['peak_value'].info.format = '%.8g'  # for consistent table output

print(tbl[:])
positions = np.transpose((tbl['x_peak'], tbl['y_peak']))
#positions=positions[44:49]
amp = np.array(tbl['peak_value'])
#amp=amp[44:49]

print(positions)
print(amp)

data = np.ravel(image)
x = np.linspace(0, image.shape[0], image.shape[0])
y = np.linspace(0, image.shape[1], image.shape[1])
x, y = np.meshgrid(x, y)


fit_w = fitting.LevMarLSQFitter()

sigma_x, sigma_y = np.std(image, axis=1), np.std(image, axis=0)

x0 = positions[0][0]
y0 = positions[0][1]

x01 = positions[1][0]
y01 = positions[1][1]

x02 = positions[2][0]
y02 = positions[2][1]

x03 = positions[3][0]
y03 = positions[3][1]

x04 = positions[4][0]
y04 = positions[4][1]
print(y0)
print(x0)

print(y01)
print(x01)

w_1 = models.Gaussian2D(amp[0], x0, y0, sigma_x[x0], sigma_y[y0])
w_2 = models.Gaussian2D(amp[1], x01, y01, sigma_x[x01], sigma_y[y01])

w_3 = models.Gaussian2D(amp[2], x02, y02, sigma_x[x02], sigma_y[y02])
w_4 = models.Gaussian2D(amp[3], x03, y03,  sigma_x[x03], sigma_y[y03])

w_5 = models.Gaussian2D(amp[4], x04, y04,  sigma_x[x04], sigma_y[y04])


yi, xi = np.indices(image.shape)

g_1 = fit_w(w_1, xi, yi, image)
g_2 = fit_w(w_2, xi, yi, image)
g_3 = fit_w(w_3, xi, yi, image)
g_4 = fit_w(w_4, xi, yi, image)
g_5 = fit_w(w_5, xi, yi, image)
print(w_1)
print(w_2)
print(w_3)
print(w_4)
print(w_5)


model_data =g_1(xi, yi) +g_2(xi, yi) +g_3(xi, yi) +g_4(xi, yi) +g_5(xi, yi) -np.mean(image)*5
apertures = CircularAperture(positions, r=5.0)
plt.imshow(image,cmap=plt.cm.gist_earth_r) 
apertures.plot(color='#0547f9', lw=1.5)
plt.show()
plt.imshow(model_data ,cmap=plt.cm.gist_earth_r)
plt.show()

plt.imshow(image - model_data ,cmap=plt.cm.gist_earth_r) 

plt.show()
