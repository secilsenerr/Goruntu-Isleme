#Morphological Filtering Morphological Gradient
import cv2
import numpy as np

resim = cv2.imread("images.jpg", 0)
binr = cv2.threshold(resim, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
kernel = np.ones((3, 3), np.uint8)
ters = cv2.bitwise_not(binr)
morph_gradient = cv2.morphologyEx(ters, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("Orijinal resim", resim)
cv2.imshow("Yeni resim", morph_gradient)
cv2.waitKey(0)

