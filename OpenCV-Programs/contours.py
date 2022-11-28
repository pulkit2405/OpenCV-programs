import cv2 as cv
import numpy as np

img = cv.imread('Images/starwars.jpg')
img = cv.resize(img, (1000,500))
cv.imshow('star wars', img)
blank = np.zeros(img.shape, dtype ='uint8')
cv.imshow('blank', blank)
#converting the image into a gray image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray image', gray)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("blurred image", blur)
canny = cv.Canny(img, 125, 175)
cv.imshow('canny  edges', canny)
#ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('contours drawn', blank)

cv.waitKey(0)