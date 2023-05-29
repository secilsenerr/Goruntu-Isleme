#Image brightness
import cv2 as cv
import numpy as np
import argparse
# Read image given by user
parser = argparse.ArgumentParser(description='Resmin parlakligini degistirme kodu')
parser.add_argument('--input', help='input resmine giden yol', default='ani.jpg')
args = parser.parse_args()
resim = cv.imread(cv.samples.findFile(args.input))
if resim is None:
    print('Resim açılamadı veya bulunamadı: ', args.input)
    exit(0)
yeni_resim = np.zeros(resim.shape, resim.dtype)
alfa = 1.0 # contrast control
beta = 0    # brightness control
try:
    alfa = float(input('Alfa değerini giriniz [1.0-3.0]: '))
    beta = int(input('Beta değerini giriniz [0-100]: '))
except ValueError:
    print('Hata, sayı değil!')

for y in range(resim.shape[0]):
    for x in range(resim.shape[1]):
        for c in range(resim.shape[2]):
            yeni_resim[y, x, c] = np.clip(alfa * resim[y, x, c] + beta, 0, 255)
cv.imshow('Orijinal resim', resim)
cv.imshow('Yeni resim', yeni_resim)
# Wait until user press some key
cv.waitKey()