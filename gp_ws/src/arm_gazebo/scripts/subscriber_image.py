#!/usr/bin/env python
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import time
import numpy as np
import message_filters

class image_converter:
    def __init__(self):
        rospy.init_node('image_converter', anonymous=True)
        self.bridge = CvBridge()
        image_sub = message_filters.Subscriber("/depth/color/image_raw", Image)
        depth_sub = message_filters.Subscriber("/depth/depth/image_raw", Image)
        self.ts = message_filters.ApproximateTimeSynchronizer([image_sub, depth_sub], 1, 1)
        self.ts.registerCallback(self.callback)
       
    def callback(self,rgb_data, depth_data):
      try:
         a= raw_input("Enter (s) to continue: ")
         if a =='s':
            rospy.loginfo("In image callback")
            image = self.bridge.imgmsg_to_cv2(rgb_data, "bgr8")
            depth_image = self.bridge.imgmsg_to_cv2(depth_data, "passthrough")
            depth_array = np.array(depth_image, dtype=np.float32)
            color_array = np.array(image, dtype=np.uint8)
            depth_array[np.isnan(depth_array)] = 0
            cv2.normalize(depth_array, depth_array, 0, 255, cv2.NORM_MINMAX)
            rospy.loginfo(image.shape)
            cv2.imwrite('/home/ceslab/camera_rgb.jpg', color_array)
            cv2.imwrite('/home/ceslab/camera_depth.png', depth_array)
            rospy.loginfo("Saved images...")               
      except CvBridgeError as e:
        print(e)
     
def main(args):
  image_converter()
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
    cv2.destroyAllWindows()
    
if __name__ == '__main__': 
    main(sys.argv)  