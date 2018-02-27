# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:50:35 2017

@author: vbhaumik
"""

import cv2
import numpy as np

img = cv2.imread('images/morph.jpg',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 2)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
cv2.imshow('gradiant',gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()