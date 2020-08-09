#!/usr/bin/env python
from std_msgs.msg import String
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

def control(key):

  hand_poses = ['pinch', 'tripod', 'neutral', 'relaxed_hand', 'pronated']
  arm_poses = ['home', 'capture', 'initial', 'final']
  
  ## First initialize `moveit_commander`_ and a `rospy`_ node:
  
  
  ## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
  ## kinematic model and the robot's current joint states
  robot = moveit_commander.RobotCommander(ns="arm_stand")
  
  ## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
  ## for getting, setting, and updating the robot's internal understanding of the
  ## surrounding world:
  scene = moveit_commander.PlanningSceneInterface()
  pose = key.data
  rospy.loginfo(pose)
  if pose in hand_poses:
    
   ## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
   ## to a planning group (group of joints).  In this tutorial the group is the primary
   ## arm joints in the Panda robot, so we set the group's name to "panda_arm".
   ## If you are using a different robot, change this value to the name of your robot
   ## arm planning group.
   ## This interface can be used to plan and execute motions:
    group_name = "hand"
   
  else:
    group_name = "arm"
     
  move_group = moveit_commander.MoveGroupCommander(group_name)
  
  move_group.set_named_target(pose)
  rospy.loginfo("here")
  ## Now, we call the planner to compute the plan and execute it.
  plan = move_group.plan()
  # Calling `stop()` ensures that there is no residual movement
  #move_group.stop()
  # It is always good to clear your targets after planning with poses.
  # Note: there is no equivalent function for clear_joint_value_targets()
  #move_group.clear_pose_targets()
  
  ## BEGIN_SUB_TUTORIAL execute_plan
  ##
  ## Executing a Plan
  ## ^^^^^^^^^^^^^^^^
  ## Use execute if you would like the robot to follow
  ## the plan that has already been computed:
  #move_group.execute(plan, wait=True)
  
  ## **Note:** The robot's current joint state must be within some tolerance of the
  ## first waypoint in the `RobotTrajectory`_ or ``execute()`` will fail
  
  rospy.sleep(2)
  
  move_group.go(wait=True)
  
  moveit_commander.roscpp_shutdown()

  return

if __name__=='__main__':

  rospy.init_node('move_group_py', anonymous=True)
  moveit_commander.roscpp_initialize(sys.argv)
  sub = rospy.Subscriber("move_type", String, control)
  rospy.spin()

       

