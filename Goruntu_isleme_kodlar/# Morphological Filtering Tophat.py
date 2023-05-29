# Morphological Filtering Top Hat
import cv2
filterSize =(3, 3)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filterSize)
resim = cv2.imread("testing2.png")
resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
tophat_resim = cv2.morphologyEx(resim, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Orijinal resim", resim)
cv2.imshow("Yeni resim", tophat_resim)
cv2.waitKey(0)
