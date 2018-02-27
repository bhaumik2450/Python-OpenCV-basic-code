# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:44:29 2017

@author: vbhaumik
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/cameraman.tif')

blur = cv2.blur(img,(5,5))
blur1 = cv2.GaussianBlur(img,(5,5),0)
median1 = cv2.medianBlur(img,5)
blur2 = cv2.bilateralFilter(img,9,75,75)

plt.subplot(321),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(blur1),plt.title('Gaussian Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(blur2),plt.title('bilateral Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(blur),plt.title('Median Blurred')
plt.xticks([]), plt.yticks([])

plt.show()

