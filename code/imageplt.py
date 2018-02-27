# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 12:10:08 2017

@author: vbhaumik
"""
import numpy as np
import matplotlib . pyplot as plt
A = np.random.random((100, 100))
plt.imshow(A)
plt.hot()
plt.colorbar()
plt.savefig('imageplot.pdf')