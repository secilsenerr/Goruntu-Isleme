#Image Enhancement techniques 
import cv2
import numpy as np

resim = cv2.imread('ani.jpg', 0)
m, n = resim.shape
L = resim.max()
resim_neg = L - resim
cv2.imwrite('Resim_Negatif.jpg', resim_neg)

T = 150

resim_thresh = np.zeros((m, n), dtype=int)

for i in range(m):

    for j in range(n):

        if resim[i, j] < T:
            resim_thresh[i, j] = 0
        else:
            resim_thresh[i, j] = 255

cv2.imwrite('Resim_Thresh.jpg', resim_thresh)

T1 = 100
T2 = 180

resim_thresh_back = np.zeros((m, n), dtype=int)

for i in range(m):

    for j in range(n):

        if T1 < resim[i, j] < T2:
            resim_thresh_back[i, j] = 255
        else:
            resim_thresh_back[i, j] = resim[i, j]

cv2.imwrite('Resim_Thresh_Back.jpg', resim_thresh_back)
