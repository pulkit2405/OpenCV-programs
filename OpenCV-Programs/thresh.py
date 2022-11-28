import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread('Images/starwars.jpg')
img = cv.resize(img, (500,250))
cv.imshow('star wars', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('simple thresholded image', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('simple thresholded inverse image', thresh_inv)

#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 15, 3)
cv.imshow('adaptive thresholded image', adaptive_thresh)

cv.waitKey(0)