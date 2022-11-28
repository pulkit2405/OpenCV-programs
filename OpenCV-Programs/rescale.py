import cv2 as cv

img = cv.imread('Images/starwars.jpg')
cv.imshow('star wars', img)

#resizing the image
resized = cv.resize(img, (1000,500))
cv.imshow('resized', resized)
#making the image blur
blur= cv.GaussianBlur(resized, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)
#seeing canny edges of a picture
canny = cv.Canny(resized, 125, 175)
cv.imshow('canny edges',canny)
#seeing the dilated version of the canny edges
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)
#seeing the eroded version of the dilated image
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

cv.waitKey(0)
