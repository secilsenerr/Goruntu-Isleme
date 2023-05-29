#Morphological Filtering Black Hat
import cv2
filtre_boyut = (3, 3)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filtre_boyut)
resim = cv2.imread("images.jpg")
resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
blackhat_resim = cv2.morphologyEx(resim, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Orijinal resim", resim)
cv2.imshow("Yeni resim", blackhat_resim)
cv2.waitKey(0)
