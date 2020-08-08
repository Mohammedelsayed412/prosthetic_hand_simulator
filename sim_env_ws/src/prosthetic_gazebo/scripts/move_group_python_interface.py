#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

## First initialize `moveit_commander`_ and a `rospy`_ node:
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

## Instantiate a `RobotCommander`_ object. Provides information such as the robot's
## kinematic model and the robot's current joint states
robot = moveit_commander.RobotCommander()

## Instantiate a `PlanningSceneInterface`_ object.  This provides a remote interface
## for getting, setting, and updating the robot's internal understanding of the
## surrounding world:
scene = moveit_commander.PlanningSceneInterface()

## Instantiate a `MoveGroupCommander`_ object.  This object is an interface
## to a planning group (group of joints).  In this tutorial the group is the primary
## arm joints in the Panda robot, so we set the group's name to "panda_arm".
## If you are using a different robot, change this value to the name of your robot
## arm planning group.
## This interface can be used to plan and execute motions:
group_name = "hand"
move_group = moveit_commander.MoveGroupCommander(group_name)

## Create a `DisplayTrajectory`_ ROS publisher which is used to display
## trajectories in Rviz:
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)
## Getting Basic Information
## ^^^^^^^^^^^^^^^^^^^^^^^^^
# We can get the name of the reference frame for this robot:
planning_frame = move_group.get_planning_frame()
print "============ Planning frame: %s" % planning_frame

# We can also print the name of the end-effector link for this group:
eef_link = move_group.get_end_effector_link()
print "============ End effector link: %s" % eef_link

# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print "============ Available Planning Groups:", robot.get_group_names()

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print "============ Printing robot state"
print robot.get_current_state()
print ""

## Planning to a Pose Goal
## ^^^^^^^^^^^^^^^^^^^^^^^
## We can plan a motion for this group to a desired pose for the
## end-effector:
#pose_goal = geometry_msgs.msg.Pose()
#pose_goal.orientation.w = 1.0
#pose_goal.position.x = 0.4
#pose_goal.position.y = 0.1
#pose_goal.position.z = 0.4

move_group.set_named_target("pinch")

## Now, we call the planner to compute the plan and execute it.
plan = move_group.plan()
# Calling `stop()` ensures that there is no residual movement
#move_group.stop()
# It is always good to clear your targets after planning with poses.
# Note: there is no equivalent function for clear_joint_value_targets()
move_group.clear_pose_targets()

## BEGIN_SUB_TUTORIAL execute_plan
##
## Executing a Plan
## ^^^^^^^^^^^^^^^^
## Use execute if you would like the robot to follow
## the plan that has already been computed:
move_group.execute(plan, wait=True)

## **Note:** The robot's current joint state must be within some tolerance of the
## first waypoint in the `RobotTrajectory`_ or ``execute()`` will fail

rospy.sleep(5)
moveit_commander.roscpp_shutdown()
