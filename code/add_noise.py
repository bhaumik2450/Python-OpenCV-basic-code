# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 11:58:42 2017

@author: vbhaumik


Parameters
----------
image : ndarray
    Input image data. Will be converted to float.
mode : str
    One of the following strings, selecting the type of noise to add:

    'gauss'     Gaussian-distributed additive noise.
    'poisson'   Poisson-distributed noise generated from the data.
    's&p'       Replaces random pixels with 0 or 1.
    'speckle'   Multiplicative noise using out = image + n*image,where
                n is uniform noise with specified mean & variance.
"""
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
def noisy(image,noise_typ):
   if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 0
      var = 0.001
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy
   elif noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 0.5
      amount = 0.04
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 1

      # Pepper mode
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out
   elif noise_typ == "poisson":
      vals = len(np.unique(image))
      vals = 2 ** np.ceil(np.log2(vals))
      noisy = np.random.poisson(image * vals) / float(vals)
      return noisy
   elif noise_typ =="speckle":
      row,col,ch = image.shape
      gauss = np.random.randn(row,col,ch)
      gauss = gauss.reshape(row,col,ch)        
      noisy = image + image * gauss
      return noisy
      
img = cv2.imread('images/cameraman.tif')

p_img = noisy(img,"gauss")
s_p_img = noisy(img,"s&p")
s_img = noisy(img,"speckle")
median1 = cv2.medianBlur(s_p_img,5)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(p_img),plt.title('gauss')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(s_p_img),plt.title('Salt and papper')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(median1),plt.title('After Median filter')
plt.xticks([]), plt.yticks([])


plt.show()
