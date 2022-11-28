import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Images/starwars.jpg')
img = cv.resize(img, (1000,500))
cv.imshow('star wars', img)

#plt.imshow(img)
#plt.show()

#converting BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#converting BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HLS)
cv.imshow('hsv', hsv)

#converting BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

plt.imshow(rgb)
plt.show

cv.waitKey(0)