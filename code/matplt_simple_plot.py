# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:44:16 2017

@author: vbhaumik
"""

import numpy as np
import matplotlib . pyplot as plt
x = np. linspace (0 , 10, 1000)
y = np.power(x , 2)
plt.plot (x , y)
plt.show()
plt.figure(2)
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
t = np.arange(0., 5., 0.2)
plt.figure(3)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
plt.figure(4)
x = np. linspace (0 , 10, 50)
y1 = np.power(x , 2)
y2 = np.power(x , 3)
plt.plot (x , y1 , 'rs' , label='x^2' )
plt.plot (x , y2 , 'go ' , label='x^3' )
plt.xlim([1 , 5])
plt.ylim([0 , 30])
plt.xlabel ( 'my x label ' )
plt.ylabel ( 'my y label ' )
plt.title( ' plot t i t l e , including Omega' )
plt.legend()
plt.show()
plt.savefig('line_plot_plus2.pdf')


