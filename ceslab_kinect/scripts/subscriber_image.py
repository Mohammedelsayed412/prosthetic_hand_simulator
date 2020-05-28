#!/usr/bin/python
import roslib
import rospy
import sys
import cv2 as cv
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

class cvBridgeDemo():
    def __init__(self):
        self.node_name = "saveing_image"

        rospy.init_node(self.node_name)

        # What we do during shutdown
        rospy.on_shutdown(self.cleanup)

        # Create the cv_bridge object
        self.bridge = CvBridge()

        # Subscribe to the camera image topics and set the appropriate callbacks
        self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.image_callback)
        rospy.loginfo("Waiting for image topics...")

    def image_callback(self, ros_image):
        # Use cv_bridge() to convert the ROS image to OpenCV format
        try:
            rospy.loginfo("trying to convert ros image to cv2")
            frame = self.bridge.imgmsg_to_cv2(ros_image, desired_encoding='passthrough')
            rospy.loginfo("coversion done successfully")
        except CvBridgeError, e:
            rospy.loginfo("Exception found ! ! !")
            print e
        
        
        # Saving the image
        rospy.loginfo("saving image")
        cv.imwrite('captured_img.jpg', frame)
        rospy.loginfo("image saved successfully in your work space named captured_img.jpg")


    def cleanup(self):
        print "Shutting down vision node."
        cv.destroyAllWindows()   

def main(args):       
    try:
        cvBridgeDemo()
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down vision node."
        cv.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)