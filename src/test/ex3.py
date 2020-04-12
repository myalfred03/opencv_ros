import cv2
import numpy as np
import matplotlib.pylab as plt
import os


img = cv2.imread('RandomColor.png')
img[:5, :5] = [255]
#img[:, :, 1] = 0  #row,column,layer RGB

#print img.item(9, 9, 2) # prints the current value of B for that pixel

#img.itemset( (9, 9, 2), 0)
#print img.item(9, 9, 2) # prints 255
print img.shape
print img.size
print img.dtype

plt.imshow(img)
#plt.imshow(hsv)
plt.show()