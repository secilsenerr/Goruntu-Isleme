#Morphological Filtering Opening
import cv2
resim = cv2.imread("beyaz.jpg")
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=1)
opening2 = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=2)

cv2.imshow("Orijinal resim", resim)
cv2.imshow("Yeni resim", opening)
cv2.imshow("Yeni resim-2", opening2)
cv2.waitKey(0)