#!/usr/bin/python
import roslib
import rospy
import sys
import cv2 as cv
import base64
import json
from PIL import Image
from io import StringIO,BytesIO 
from sensor_msgs.msg import Image, CameraInfo
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

class cvBridgeDemo():
    def __init__(self):
        self.node_name = "saving image"
        rospy.init_node(self.node_name)
        
        # What we do during shutdown
        rospy.on_shutdown(self.cleanup)

        # Create the cv_bridge object
        self.bridge = CvBridge()

        # Subscribe to the camera image topics and set the appropriate callbacks
        self.image_sub = rospy.Subscriber("/camera1/image_raw", Image, self.image_callback)
        self.trigger_sub = rospy.Subscriber("/teleop_key", String, self.flag_update)
        self.old_flag = "quit"
        self.flag = False
        rospy.loginfo("Waiting for image topics...")
        
    def flag_update(self, ros_key):
        if self.old_flag != ros_key.data :
            if ros_key.data == "start" :
                self.flag = True
                self.old_flag = ros_key.data
            else : 
                self.flag = False
                self.old_flag = ros_key.data
            rospy.loginfo(ros_key)   
    
    def image_callback(self, ros_image):
        # Use cv_bridge() to convert the ROS image to OpenCV format
        rospy.loginfo("In image callback")
        if self.flag :
            try:
                rospy.loginfo("trying to convert ros image to cv2")
                frame = self.bridge.imgmsg_to_cv2(ros_image, desired_encoding='passthrough')
                rospy.loginfo("coversion done successfully")
            except CvBridgeError, e:
                rospy.loginfo("Exception found ! ! !")
                print e
            
            # initializing IP adress to send request
            addr = 'http://localhost:4000'  ## the API adress
            url = addr + '/api/model/'
            retval, buffer = cv.imencode('.jpg', frame) #Encoding CV format to JPG
            data = base64.b64encode(buffer) #Serializing Image to Base64
            ## sending request
            request = requests.post(url, json={'img_base64':data})
            rospy.loginfo("Image Sent to Server")
            self.flag = False
        

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