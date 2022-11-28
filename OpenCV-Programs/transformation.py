import cv2 as cv
import numpy as np

img = cv.imread('Images/starwars.jpg')
resized = cv.resize(img, (1000,500))
cv.imshow('resized', resized)
#Translation
#repositioning in the same window
#-x : left
#-y : top  
#x : right
#y : bottom
def translate(img, x, y):
    transMat =np.float32([[1,0,x],[0,1,y]])
    dimensions =(img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
translated = translate(resized, -100, -100)
cv.imshow('translated', translated)
#Rotation
#positive angle of rotation : anti-clockwise rotation
#negative angle of rotation : clockwise rotation
def rotate(img, angle, rotPoint= None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotate(resized, 90)
cv.imshow('rotated', rotated)
#flipping the image
flip = cv.flip(resized, 1)
cv.imshow('flip',flip)
cv.waitKey(0)