# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 12:04:43 2017

@author: vbhaumik
"""
import numpy as np
import matplotlib.pyplot as plt
data = np.random. randn(1000)
f,(ax1,ax2) = plt.subplots(1 , 2, figsize=(6,3))
# histogram (pdf)
ax1.hist (data , bins=30, normed=True, color='b' )
# empirical cdf
ax2.hist (data , bins=30, normed=True, color='r',cumulative=True)
plt.savefig('histogram.pdf')
