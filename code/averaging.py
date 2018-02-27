# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:42:22 2017

@author: vbhaumik
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/cameraman.tif')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()