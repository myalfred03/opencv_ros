#!/usr/bin/env python    

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import sys
import rospy
import cv2
import time
import matplotlib.pylab as plt
import numpy as np

from std_msgs.msg           import String
from sensor_msgs.msg        import Image
from geometry_msgs.msg      import Point
from cv_bridge              import CvBridge, CvBridgeError

from include.lib_detector_ros  import *

class LaneDetector:

	def __init__(self):

		print (">> Publishing image to topic image_blob")
		self.image_pub = rospy.Publisher("/lane/image_lane",Image,queue_size=1)
		self.mask_pub = rospy.Publisher("/lane/image_mask",Image,queue_size=1)
		print (">> Publishing position to topic point_blob")
		self.blob_pub  = rospy.Publisher("/lane/point_lane",Point,queue_size=1)

		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/image_raw",Image,self.callback)
		print ("<< Subscribed to topic /image_raw camera pc")

	def callback(self,data):
			
			#--- Assuming image is 320x240
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)

		 
		try:
			self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
			#self.mask_pub.publish(self.bridge.cv2_to_imgmsg(mask, "8UC1"))
		except CvBridgeError as e:
			print(e)            

def main(args):
	img = np.zeros((3,3), dtype=np.uint8)
	img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

	ic = LaneDetector()
	rospy.init_node('lane_detector', anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)
