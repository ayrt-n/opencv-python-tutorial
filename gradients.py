import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('La', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('X', sobelx)
cv.imshow('Y', sobely)
combined = cv.bitwise_or(sobelx, sobely)
cv.imshow('comb', combined)

# Canny for comparison
canny = cv.Canny(gray, 150, 175)
cv.imshow('Can', canny)


cv.waitKey(0)