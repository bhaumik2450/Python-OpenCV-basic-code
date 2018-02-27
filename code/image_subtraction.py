# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:55:56 2017

@author: vbhaumik
"""

import cv2
img1 = cv2.imread('images/cameraman.tif')
cv2.imshow('img1',img1)
img2 = cv2.imread('images/circles.png')
cv2.imshow('img2',img2)
dst = cv2.addWeighted(img1,1,img2,1,0)

cv2.imshow('dst',dst)
sub=cv2.subtract(img1,img2)
cv2.imshow('subtract',sub)


inv= cv2.bitwise_not(img2)
cv2.imshow('inverse',inv)
if cv2.waitKey(0) & 0xFF == 27 :
    cv2.destroyAllWindows()