#Histogram Equalization
import cv2
import numpy
img = cv2.imread('kiz.jpg')
img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_esitleme_sonuc = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
cv2.imwrite('sonuc.jpg', hist_esitleme_sonuc)