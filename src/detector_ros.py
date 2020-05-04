#!/usr/bin/env python    

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import sys
import rospy
import rospkg
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

    def __init__(self, cap):

        self.cap = cap

        print (">> Publishing image to topic image_blob")
        self.image_pub = rospy.Publisher("/lane/image_lane",Image,queue_size=1)
        self.mask_pub = rospy.Publisher("/lane/image_mask",Image,queue_size=1)
        self.video_pub = rospy.Publisher("/lane/video",Image,queue_size=1)

        print (">> Publishing position to topic point_blob")
        self.blob_pub  = rospy.Publisher("/lane/point_lane",Point,queue_size=1)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/image_raw",Image,self.callback)
        print ("<< Subscribed to topic /image_raw camera pc")

        self.read()

    def read(self):
     
        try:

            if not self.cap.isOpened():
                rospy.logerr('Failed to open file')
                exit(1)
            while self.cap.isOpened():

                ret, frame = self.cap.read()
                blur = deNoise(frame)
                gray_image = edgeDetector(blur)
               # canny_image = cv2.Canny(gray_image, 160, 210)
                self.video_pub.publish(self.bridge.cv2_to_imgmsg(gray_image, "8UC1")) #8UC1   bgr8
                #if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except CvBridgeError as e:
            print(e)

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            print ("subscribe video camera")

            gray_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2GRAY)
            canny_image = cv2.Canny(gray_image, 160, 210)
            
        except CvBridgeError as e:
            print(e)

        self.read()


            # try:
            #   self.cap = cv2.VideoCapture('project_video.mp4')
            #   while self.cap.isOpened():
            #       print ("reading video")

            #       ret, frame = self.cap.read()
            #       try:
            #           self.video_pub.publish(self.bridge.cv2_to_imgmsg(frame, "8UC1"))

            #       except CvBridgeError as e:
            #           print(e)    

            # except CvBridgeError as e:
            #   print(e)

            #--- Assuming image is 320x240


         
        # try:
        #   #self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
        #   #self.mask_pub.publish(self.bridge.cv2_to_imgmsg(mask, "8UC1"))
        #   self.video_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "8UC1"))

        # except CvBridgeError as e:
        #   print(e)            


# while cap.isOpened():
#   print ("reading video")

#   ret, frame = cap.read()

def main(args):
    rospy.init_node('lane_detector', anonymous=True)
    rospack = rospkg.RosPack()
    filevideo = rospack.get_path('opencv_ros') + '/src/project_video.mp4'

    img = np.zeros((3,3), dtype=np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    cap = cv2.VideoCapture(filevideo)

    # if not cap.isOpened():
    #   rospy.logerr('Failed to open file')
    #   exit(1)
    # while cap.isOpened():

    #   ret, frame = cap.read()

    #   try:
    #       rospy.spin()
    #   except KeyboardInterrupt:
    #       print("Shutting down")
    ic = LaneDetector(cap)

    #   if cv2.waitKey(1) & 0xFF == ord('q'):
    #       break
    #ic.run()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)