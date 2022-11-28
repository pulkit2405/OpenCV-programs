import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread('Images/starwars.jpg')
img = cv.resize(img, (500,250))
cv.imshow('star wars', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

circle =cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', circle)

masked = cv.bitwise_and(gray, gray, mask= circle)
cv.imshow('masked image', masked)

#Gray scale histogram
gray_hist = cv.calcHist([gray], [0], masked,[256], [0,256])

plt.figure()
plt.title('gray histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


cv.waitKey(0)