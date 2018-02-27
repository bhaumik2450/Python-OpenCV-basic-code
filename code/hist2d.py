# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:36:16 2017

@author: vbhaumik
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('images/autumn.tif')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
plt.subplot(1,2,1),plt.imshow(img), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(hist,interpolation = 'nearest'), plt.xticks([]), plt.yticks([])
plt.show()
