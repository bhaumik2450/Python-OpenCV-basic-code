# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 09:30:39 2017

@author: vbhaumik
"""
import cv2

img1 = cv2.imread('messi5.jpg')

e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t