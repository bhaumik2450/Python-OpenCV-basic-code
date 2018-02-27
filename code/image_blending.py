# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 09:29:12 2017

@author: vbhaumik
"""

import cv2
img1 = cv2.imread('images/cameraman.tif',0)
cv2.imshow('img1',img1)
img2 = cv2.imread('images/circles.png',0)
cv2.imshow('img2',img2)
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()