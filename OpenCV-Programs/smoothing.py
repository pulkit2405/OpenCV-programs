import cv2 as cv 

img = cv.imread('Images/starwars.jpg')
img= cv.resize(img, (500,250))
cv.imshow('star wars', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('average image', average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian blur', gauss)

#Median blur
median = cv.medianBlur(img, 3)
cv.imshow('median blur', median)

#bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)