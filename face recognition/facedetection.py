import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv.imread('photo.jpg')
#img = cv.resize(img, (500,250))
cv.imshow('person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray person', gray)


faces_rect = haar_cascade.detectMultipleScale(gray, scaleFactor=1.1, minNeighbors = 3)
print(f'Number of faces found ={len(faces_rect)}')

for(x, y , w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow('detected faces', img)

cv.waitKey(0)
