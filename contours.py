import cv2 as cv
import numpy as np

# Contours and edges are different but can get away with thinking about them similarily. Contours are helpful for shape analysis
img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Can use canny edge detection or thresholds to find contours
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Looks at image and tries to binarize image
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# Looks at structuring element (edges) and returns contours (python list of all coordinates) and hierachies
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'Contours: {len(contours)}')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours', blank)



cv.waitKey(0)