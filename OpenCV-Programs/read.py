import cv2 as cv
import numpy as np 

#making a blank image for experimenting
blank= np.zeros((750,750), dtype='uint8')
cv.imshow('blank', blank)
#rectangle
cv.rectangle(blank, (50,50), (500,500),(69,69,69), thickness=2) 
cv.imshow('rectangle', blank)
#entering text on image
cv.putText(blank, 'HelloWorld!',(100,250), fontFace=cv.FONT_HERSHEY_SCRIPT_COMPLEX, fontScale=2.0, color=(255,0,0), thickness=4)
cv.imshow('text', blank)
cv.waitKey(0)