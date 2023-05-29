#Morphological Filtering Closing
import cv2
resim = cv2.imread("close.png")
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel, iterations=1)
closing2 = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel, iterations=2)

cv2.imshow("Orijinal resim", resim)
cv2.imshow("Yeni resim", closing)
cv2.imshow("Yeni resim-2", closing2)
cv2.waitKey(0)