# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 13:08:53 2017

@author: vbhaumik
"""
import numpy as np
import cv2
np.set_printoptions(threshold=np.inf)
#img = cv2.imread('C:/Users/vbhaumik/Pictures/Capture.jpg',0)
img = cv2.imread('images/messi5.jpg',0)

print img

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
cv2.imshow('first_image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()