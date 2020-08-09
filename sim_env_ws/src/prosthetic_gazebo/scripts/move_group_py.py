#!/usr/bin/env python
from std_msgs.msg import String
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg

def control(key):  
  hand_poses = ['pinch', 'tripod', 'neutral', 'relaxed_hand', 'pronated']
  arm_poses = ['home', 'capture', 'initial', 'final']
  moveit_commander.roscpp_initialize(sys.argv)
  robot = moveit_commander.RobotCommander(ns="arm_stand")
  scene = moveit_commander.PlanningSceneInterface()
  pose = key.data
  rospy.loginfo(pose)
  
  if pose in hand_poses:
    group_name = "hand"
  else:
    group_name = "arm"
     
  move_group = moveit_commander.MoveGroupCommander(group_name)
  
  move_group.set_named_target(pose)
  rospy.loginfo("here")
  ## Now, we call the planner to compute the plan and execute it.
  plan = move_group.plan()
  
  rospy.sleep(2)
  
  move_group.go(wait=True)
  
  moveit_commander.roscpp_shutdown()

def listener():
  rospy.init_node('listener', anonymous=True)
  rospy.Subscriber("move_type", String, control)
  rospy.spin()
  

if __name__ == '__main__':
  listener()

