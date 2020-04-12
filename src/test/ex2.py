import cv2
import numpy as np
import matplotlib.pylab as plt
import os

# Make an array of 120,000 random bytes.
randomByteArray = bytearray(os.urandom(300))
flatNumpyArray = np.array(randomByteArray)
#grayImage = flatNumpyArray.reshape(300, 400)
bgrImage = flatNumpyArray.reshape(10, 10, 3)

print(bgrImage)
plt.imshow(bgrImage)
#plt.imshow(hsv)
plt.show()