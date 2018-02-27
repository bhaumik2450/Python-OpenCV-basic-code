# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:03:30 2017

@author: vbhaumik
"""

import cv2
import numpy as np

img = cv2.imread('images/cameraman.tif',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)


img = cv2.imread('images/cameraman.tif',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img1',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()