# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:36:04 2017

@author: vbhaumik
"""

import cv2
import numpy as np

img = cv2.imread('star.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print M