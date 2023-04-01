from scipy import fft
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

hdul_1 = fits.open('noised.fits')
image=hdul_1[0].data
ft_img = fft.fft2(image) 

#plt.imshow(np.abs(ft_img)  , cmap= 'gray',norm=LogNorm(vmin=0.01, vmax=1))
px1=(15,15)
px2=(1623,1778)

ft_img[px1] = np.median(ft_img[px1[0] - 1:px1[0] + 1, px1[1] - 1:px1[1] + 1])
ft_img[px2] = np.median(ft_img[px2[0] - 1:px2[0] + 1, px2[1] - 1:px2[1] + 1])

#plt.imshow(np.abs(ft_img)  , cmap= 'gray',norm=LogNorm(vmin=0.01, vmax=1))
image = np.abs(fft.fft2(ft_img))
hdu = fits.PrimaryHDU(image)
hdul_2 = fits.HDUList([hdu])
hdul_2.writeto('without_noise.fits')

