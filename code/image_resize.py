# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:02:46 2017

@author: vbhaumik
"""

import cv2
import numpy as np

img = cv2.imread('images/messi5.jpg')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('res1',res)
#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()