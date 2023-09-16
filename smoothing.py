import cv2 as cv
import numpy as np

# Bluring/smoothing can help remove noise in images
img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Average', average)

# Gaussian
gaus = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaus', gaus)

# Median
median = cv.medianBlur(img, 7)
cv.imshow('Median', median)

# Bilateral
bil = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bil', bil)

cv.waitKey(0)
