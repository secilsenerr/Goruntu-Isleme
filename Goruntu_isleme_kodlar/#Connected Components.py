#Connected Components
import cv2
import numpy as np

resim = cv2.imread('yazi.jpg')
gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gri_resim, (7, 7), 0)
threshold = cv2.threshold(blurred, 0, 255,
                          cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

analiz = cv2.connectedComponentsWithStats(threshold,
                                          4,
                                          cv2.CV_32S)
(totalLabels, label_ids, values, centroid) = analiz
cikti = np.zeros(gri_resim.shape, dtype="uint8")
for i in range(1, totalLabels):

    alan = values[i, cv2.CC_STAT_AREA]

    if (alan > 140) and (alan < 400):
        componentMask = (label_ids == i).astype("uint8") * 255
        cikti = cv2.bitwise_or(cikti, componentMask)

cv2.imshow("Orijinal Resim", resim)
cv2.imshow("Yeni Resim", cikti)
cv2.waitKey(0)
