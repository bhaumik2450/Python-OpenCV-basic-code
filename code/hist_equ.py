# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:54:50 2017

@author: vbhaumik
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('images/rice.png',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imshow("img",res)
