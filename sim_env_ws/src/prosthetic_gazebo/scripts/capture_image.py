#!/usr/bin/python
import getch
import rospy
from std_msgs.msg import String  

def keys():
    pub = rospy.Publisher('teleop_key', String, queue_size=10) # where teleop_key is the name of the topic 
    rospy.init_node('keypress',anonymous=True) # whare keypress is the name of the node
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        k = ord(getch.getch())
        dic = {115:"start", 113:"quit", 110:"neutral", 114:"pronated", 112:"pinch", 116:"tripod"}    # 115-> s key, 113-> q key # n, r, p, t
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