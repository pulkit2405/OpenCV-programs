import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 175, 255, -1)
cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

#bitwise AND
bitwise_and = cv.bitwise_and(circle, rectangle)
cv.imshow('bitwise and', bitwise_and)

#bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise or', bitwise_or)

#bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise xor', bitwise_xor)

#bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('bitwise not', bitwise_not)

cv.waitKey(0)