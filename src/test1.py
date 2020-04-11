import sys
import rospy
import cv2
import numpy as np
import matplotlib.pylab as plt


frame = cv2.imread('2.jpg')
hsv   = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_blue = np.array([60, 40, 40])
upper_blue = np.array([150, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
edges = cv2.Canny(mask, 200, 400)
cv2.imshow('B/W', frame)
plt.imshow(edges)
#plt.imshow(hsv)
plt.show()

# def main(args):

# 	rospy.init_node('blob_detector', anonymous=True)
#     try:
#         rospy.spin()
#     except KeyboardInterrupt:
#         print("Shutting down")

# if __name__ == '__main__':
#     main(sys.argv)