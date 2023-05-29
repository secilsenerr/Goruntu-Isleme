#Canny Edge Detection
import cv2
import numpy as np
goruntu = cv2.imread('orn.jpg',0)
yukseklik, genislik = goruntu.shape
canny = cv2.Canny(goruntu,100,190)
cv2.imshow('Canny',canny)
cv2.waitKey(0)