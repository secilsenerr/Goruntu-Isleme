#Smoothing (Lowpass) Spatial Filter
import cv2
import numpy as np

resim = cv2.imread('tuz.jpg', 0)

m, n = resim.shape
mask = np.ones([3, 3], dtype=int)
mask = mask / 9
yeni_resim = np.zeros([m, n])

for i in range(1, m - 1):
    for j in range(1, n - 1):
        temp = resim[i - 1, j - 1] * mask[0, 0] + resim[i - 1, j] * mask[0, 1] + resim[i - 1, j + 1] * mask[0, 2] + resim[
            i, j - 1] * mask[1, 0] + resim[i, j] * mask[1, 1] + resim[i, j + 1] * mask[1, 2] + resim[i + 1, j - 1] * mask[
                   2, 0] + resim[i + 1, j] * mask[2, 1] + resim[i + 1, j + 1] * mask[2, 2]

        yeni_resim[i, j] = temp

yeni_resim = yeni_resim.astype(np.uint8)
cv2.imwrite('Yeni hali', yeni_resim)
