import cv2
import numpy as np
import matplotlib.pylab as plt

#Theory image like a vectors
#Image of three channels BGR.

img = np.zeros((3,3), dtype=np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

#Open image and convert to grayscale.
grayImage = cv2.imread('2.jpg', cv2.IMREAD_LOAD_GDAL)
cv2.imwrite('Depth.png', grayImage)


print(img.shape)
plt.imshow(img)
#plt.imshow(hsv)
plt.show()