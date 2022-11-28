import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread('Images/starwars.jpg')
img = cv.resize(img, (500,250))
cv.imshow('star wars', img)

blank = np.zeros(img.shape[:2], dtype='uint8')



mask =cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask= mask)
cv.imshow('masked image', masked)

#color histogram
plt.figure()
plt.title('color histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask
    , [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim(0,256)
plt.show()

cv.waitKey(0)