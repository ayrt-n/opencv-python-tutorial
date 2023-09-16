import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rec', rectangle)
cv.imshow('Cir', circle)

# bitwise AND
bit_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bit_and', bit_and)

# bitwise OR
bit_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitor', bit_or)

# bitwise XOR
bit_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitxor', bit_xor)

# bitwise NOT
bit_not = cv.bitwise_not(rectangle)
cv.imshow('not', bit_not)

cv.waitKey(0)