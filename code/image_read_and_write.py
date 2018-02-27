# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2

np.set_printoptions(threshold=np.inf)
#img = cv2.imread('C:/Users/vbhaumik/Pictures/Capture.jpg',0)
img = cv2.imread('images/fabric.png',0)
cv2.imshow('first_image',img)
print(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#k = cv2.waitKey(0) & 0xFF
# =============================================================================
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.imwrite('C:/Users/vbhaumik/Pictures/Capture.png',img)
#     cv2.destroyAllWindows()
# 
# =============================================================================
