import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Cat', img)

# Converting to grayscale - Only see intensity distribution of pixels, as opposed to colors themselves
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blurring - Removes some noise existing in image (e.g., bad lighting)
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade - Finding edges present in image
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Dilate Image using Structuring Element
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resize', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)