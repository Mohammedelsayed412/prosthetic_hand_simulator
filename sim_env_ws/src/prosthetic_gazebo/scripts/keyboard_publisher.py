#!/usr/bin/python
import getch
import rospy
from std_msgs.msg import String  

def keys():
    pub = rospy.Publisher('move_type', String, queue_size=10) # where teleop_key is the name of the topic 
    rospy.init_node('keyboard_control',anonymous=True) # whare keypress is the name of the node
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        k = chr(ord(getch.getch()))
        dic = {'p':"pinch", 't':"tripod", 'n':"neutral", 'r':"relaxed_hand", 'o':"pronated", 'h':"home", 'c':"capture", 'i':"initial", 'f':"final"}   
        try:
	        rospy.loginfo(dic[k])
	        pub.publish(dic[k]) 
        except KeyError:
		rospy.loginfo('key not found!')
                
if __name__=='__main__':
    try:
        keys()
    except rospy.ROSInterruptException as e:
        rospy.loginfo(e)