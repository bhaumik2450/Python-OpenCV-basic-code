# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:26:00 2017

@author: vbhaumik
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/messi5.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()