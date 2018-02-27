# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 11:51:19 2017

@author: vbhaumik
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/vbhaumik/Pictures/Capture.jpg',0)
plt.imshow(img, cmap = 'gray')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()