import cv2 as cv
import numpy as np

img = cv.imread('Images/starwars.jpg')
img = cv.resize(img, (500,250))
cv.imshow('star wars', img)

b, g, r = cv.split(img)
#the split function splits the image into color channels and display it in the grayscale

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged image', merged)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank' , blank)
#if we wish to see the color channels in the color format , we will have to do this
 
blue = cv.merge([b,blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

cv.waitKey(0)