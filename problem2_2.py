from scipy import fftpack
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import cv2

original= cv2.imread('frogs.jpg')
fourier_image = [fftpack.fft2(original[:, :, i]) for i in range(original.shape[2])]
qualities = []
sigmas = []

for p in range(4, 104, 4):
    reconstructed = []
    qual = []
    for i in range(len(fourier_image)):
        f_img = fourier_image[i]
        q = np.percentile(np.abs(f_img), 100 - p)
        rec_img = np.where(np.abs(f_img) > q, f_img, 0)
        reconstructed.append(np.abs(fftpack.ifft2(rec_img)))
        qual.append(np.sum(np.where(original[:, :, i] > 0, (original[:, :, i] - reconstructed[i]) ** 2 / original[:, :, i], 0)))
    qualities.append(np.mean(qual))
    sigmas.append(np.std(qual))

plt.xlabel("Proportion of saved coefficients, %")
plt.ylabel("Quality")
plt.errorbar(range(4, 104, 4), qualities, yerr=sigmas, fmt="o")
fig = plt.gcf()
fig.set_size_inches(12, 6)
fig.savefig("result.png", dpi=250)
plt.show()






#    rec_res = np.array(reconstructed)
#    rec_res1 = np.ndarray(shape=(rec_res.shape[1], rec_res.shape[2], rec_res.shape[0]), dtype=rec_res.dtype)
#    for i in range(rec_res.shape[0]):
#        rec_res1[:, :, i] = rec_res[i, :, :]
#    rec_res = rec_res1
#    cv2.imwrite(f"res{p}.bmp", rec_res)
