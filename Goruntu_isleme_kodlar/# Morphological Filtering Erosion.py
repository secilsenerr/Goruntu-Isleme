#Morphological Filtering Eresion
import cv2
resim = cv2.imread("images.jpg")
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
erezyon = cv2.erode(gray, kernel, iterations=1)
cv2.imshow("Orijinal resim", resim)
cv2.imshow("Yeni resim", erezyon)
cv2.waitKey(0)