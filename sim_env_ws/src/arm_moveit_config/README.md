# Must install
1. install getch library: `$ pip install getch` you can try this `$ pip install https://pypi.python.org/packages/source/g/getch/getch-1.0-python2.tar.gz` if you receive errors from the previous command.
2. 
```shell
sudo apt-get update
sudo apt-get install ros-melodic-moveit
sudo apt-get install ros-melodic-moveit-ros-visualization
sudo apt-get install ros-melodic-rviz-visual-tools
sudo apt-get dist-upgrade

sudo apt-get install ros-melodic-robot-state-publisher
sudo apt-get install ros-melodic-rviz
```

# To adjust predefined poses and joint groups to be controlled
```shell
roslaunch moveit_setup_assistant setup_assistant.launch
```
* Then either choose modify existing package "arm_moveit_config" to use moveit on our armstand and tiago hand or create a new package and upload the robot description "ur_robot.urdf.xacro" file you want to use moveit on.
** To create a new package follow this link: https://ros-planning.github.io/moveit_tutorials/doc/setup_assistant/setup_assistant_tutorial.html but for the end-effector (hand group) don't choose a kinematics solver. And for ros controller you can either follow the tutorial or press the "auto add FollowJointsTrajectory Controller" --> in config folder in kinematics.yaml add the line= "position_only_ik: True"
** To modify existing package: Adjust predefined poses or add new ones using robot poses tab

# For our robot:
1. groups: hand, arm
2. poses: hand (pinch or tripod or neutral or pronated or relaxed_hand), arm (home)

# General moveit tutorials:
1. Standard docs: https://ros-planning.github.io/moveit_tutorials/
2. Connecting moveit to gazebo: 

# Run commands:
1. To show planning and execution in RVIZ and control using RVIZ GUI:
```shell
roslaunch arm_moveit_config demo.launch 
```
2. To control arm using python script and show its movements in RVIZ: (Tutorial) https://ros-planning.github.io/moveit_tutorials/doc/move_group_python_interface/move_group_python_interface_tutorial.html 
* The code run uses predefined pose as goal pose for arm to change predefined pose change its name to:
    ** group=hand: pinch or tripod or neutral or pronated or relaxed_hand
    ** group=arm: home 
```shell
roslaunch arm_moveit_config demo.launch 
rosrun prosthetic_gazebo move_group_python_interface.py
```

3. Control using terminal: https://ros-planning.github.io/moveit_tutorials/doc/moveit_commander_scripting/moveit_commander_scripting_tutorial.html
```shell
rosrun moveit_commander moveit_commander_cmdline.py
use hand
go relaxed_hand
quit
```

# Gazebo control
1. Control using rqt_joint_controller_gui with moveit produced controllers:
```shell
roslaunch prosthetic_gazebo arm_gazebo.launch
rosrun rqt_joint_trajectory_controller rqt_joint_trajectory_controller
```
2. Control using moveit and rviz gui
```shell
roslaunch prosthetic_gazebo arm_gazebo.launch
roslaunch arm_control arm_moveit_control_rviz.launch
```
3. Control using script

3. sltns: either change PID parameters for hand like for arm in ros_controllers.yaml (failed), or add goal constraint to each joint https://github.com/tu-darmstadt-ros-pkg/hector_tracker_gazebo/blob/master/hector_tracker_gazebo_ros_control/config/default_controllers.yaml#L42 in both joints in ros_controller.yaml (failed), or do C++ code for control setting both ===> two erors goal_tolerance_violated and start position different




# Gazebo connection
1.by following this tutorial: https://github.com/tahsinkose/moveit_tutorials/commit/abce82e6a6040cb975b871389f23d5e95b4c2211 but for the movit_config package the ros_controllers.yaml config file edited to: (add arm_stand namespace)
```yaml
moveit_sim_hw_interface:
  joint_model_group: hand
  joint_model_group_pose: relaxed_hand
# Settings for ros_control_boilerplate control loop
generic_hw_control_loop:
  loop_hz: 300
  cycle_time_error_threshold: 0.01
# Settings for ros_control hardware interface
hardware_interface:
  joints:
    - joint_base_mid
    - joint_mid_top
    - joint_top_fore
    - hand_index_abd_joint
    - hand_index_virtual_1_joint
    - hand_index_flex_1_joint
    - hand_index_virtual_2_joint
    - hand_index_flex_2_joint
    - hand_index_virtual_3_joint
    - hand_index_flex_3_joint
    - hand_index_joint
    - hand_little_abd_joint
    - hand_little_virtual_1_joint
    - hand_little_flex_1_joint
    - hand_little_virtual_2_joint
    - hand_little_flex_2_joint
    - hand_little_virtual_3_joint
    - hand_little_flex_3_joint
    - hand_middle_abd_joint
    - hand_middle_virtual_1_joint
    - hand_middle_flex_1_joint
    - hand_middle_virtual_2_joint
    - hand_middle_flex_2_joint
    - hand_middle_virtual_3_joint
    - hand_middle_flex_3_joint
    - hand_mrl_joint
    - hand_ring_abd_joint
    - hand_ring_virtual_1_joint
    - hand_ring_flex_1_joint
    - hand_ring_virtual_2_joint
    - hand_ring_flex_2_joint
    - hand_ring_virtual_3_joint
    - hand_ring_flex_3_joint
    - hand_thumb_abd_joint
    - hand_thumb_virtual_1_joint
    - hand_thumb_flex_1_joint
    - hand_thumb_virtual_2_joint
    - hand_thumb_flex_2_joint
    - hand_thumb_joint
  sim_control_mode: 1  # 0: position, 1: velocity
# Publish all joint states
# Creates the /joint_states topic necessary in ROS
arm_stand:
  joint_state_controller:
    type: joint_state_controller/JointStateController
    publish_rate: 50
  hand_controller:
    type: effort_controllers/JointTrajectoryController
    joints:
      - hand_index_abd_joint
      - hand_index_virtual_1_joint
      - hand_index_flex_1_joint
      - hand_index_virtual_2_joint
      - hand_index_flex_2_joint
      - hand_index_virtual_3_joint
      - hand_index_flex_3_joint
      - hand_index_joint
      - hand_little_abd_joint
      - hand_little_virtual_1_joint
      - hand_little_flex_1_joint
      - hand_little_virtual_2_joint
      - hand_little_flex_2_joint
      - hand_little_virtual_3_joint
      - hand_little_flex_3_joint
      - hand_middle_abd_joint
      - hand_middle_virtual_1_joint
      - hand_middle_flex_1_joint
      - hand_middle_virtual_2_joint
      - hand_middle_flex_2_joint
      - hand_middle_virtual_3_joint
      - hand_middle_flex_3_joint
      - hand_mrl_joint
      - hand_ring_abd_joint
      - hand_ring_virtual_1_joint
      - hand_ring_flex_1_joint
      - hand_ring_virtual_2_joint
      - hand_ring_flex_2_joint
      - hand_ring_virtual_3_joint
      - hand_ring_flex_3_joint
      - hand_thumb_abd_joint
      - hand_thumb_virtual_1_joint
      - hand_thumb_flex_1_joint
      - hand_thumb_virtual_2_joint
      - hand_thumb_flex_2_joint
      - hand_thumb_joint
    gains:
      hand_index_abd_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_index_virtual_1_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_index_flex_1_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_index_virtual_2_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_index_flex_2_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_index_virtual_3_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_index_flex_3_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_index_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_little_abd_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_little_virtual_1_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_little_flex_1_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_little_virtual_2_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_little_flex_2_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_little_virtual_3_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_little_flex_3_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_middle_abd_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_middle_virtual_1_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_middle_flex_1_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_middle_virtual_2_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_middle_flex_2_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_middle_virtual_3_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_middle_flex_3_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_mrl_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_ring_abd_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_ring_virtual_1_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_ring_flex_1_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_ring_virtual_2_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_ring_flex_2_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_ring_virtual_3_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_ring_flex_3_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_thumb_abd_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_thumb_virtual_1_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_thumb_flex_1_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_thumb_virtual_2_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_thumb_flex_2_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
      hand_thumb_joint: {p: 50,  d: 0.1,  i: 0.1, i_clamp: 1}
  arm_controller:
    type: effort_controllers/JointTrajectoryController
    joints:
      - joint_base_mid
      - joint_mid_top
      - joint_top_fore
    gains:
      joint_base_mid: { p: 12000, d: 50, i: 0.0, i_clamp: 10000 }
      joint_mid_top: { p: 12000, d: 50, i: 0.0, i_clamp: 10000 }
      joint_top_fore: { p: 12000, d: 50, i: 0.0, i_clamp: 10000 }
      
controller_list:
  - name: arm_stand/hand_controller
    action_ns: follow_joint_trajectory
    default: True
    type: FollowJointTrajectory
    joints:
      - hand_index_abd_joint
      - hand_index_virtual_1_joint
      - hand_index_flex_1_joint
      - hand_index_virtual_2_joint
      - hand_index_flex_2_joint
      - hand_index_virtual_3_joint
      - hand_index_flex_3_joint
      - hand_index_joint
      - hand_little_abd_joint
      - hand_little_virtual_1_joint
      - hand_little_flex_1_joint
      - hand_little_virtual_2_joint
      - hand_little_flex_2_joint
      - hand_little_virtual_3_joint
      - hand_little_flex_3_joint
      - hand_middle_abd_joint
      - hand_middle_virtual_1_joint
      - hand_middle_flex_1_joint
      - hand_middle_virtual_2_joint
      - hand_middle_flex_2_joint
      - hand_middle_virtual_3_joint
      - hand_middle_flex_3_joint
      - hand_mrl_joint
      - hand_ring_abd_joint
      - hand_ring_virtual_1_joint
      - hand_ring_flex_1_joint
      - hand_ring_virtual_2_joint
      - hand_ring_flex_2_joint
      - hand_ring_virtual_3_joint
      - hand_ring_flex_3_joint
      - hand_thumb_abd_joint
      - hand_thumb_virtual_1_joint
      - hand_thumb_flex_1_joint
      - hand_thumb_virtual_2_joint
      - hand_thumb_flex_2_joint
      - hand_thumb_joint
  - name: arm_stand/arm_controller
    action_ns: follow_joint_trajectory
    default: True
    type: FollowJointTrajectory
    joints:
      - joint_base_mid
      - joint_mid_top
      - joint_top_fore

```

2. Added this line to arm_gazebo.launch file found in prosthetic_gazebo package:
```xml
<include file="$(find arm_moveit_config)/launch/ros_controllers.launch"/>
```
3. Made a new launch file in arm_control package called arm_moveit_control.launch to launch moveit control.


# Problems 
1. tiago hand joint values causes robot to be always in collision. Soltn: scaling all collision element geometry mesh tag to 0.02 0.02 tiago_description package hand urdf files. 
2. Could not find the planner configuration 'None' on the param server. Soltn: https://answers.ros.org/question/344106/could-not-find-the-planner-configuration-none-on-the-param-server/
3. No active joints or end effectors found for group 'hand'. Make sure that kinematics.yaml is loaded in this node's namespace. Soltn: Maybe change hand group to chain and use KDLkinematics solver --> didnt try it
4. Gazebo connection with rviz problems: 1. goal tolerance violated and 2. drift of joints in gazebo from position in rviz causes plans execution failure ==> **NO SOLUTION**