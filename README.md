# First Terminal
## Must install 
```bash
sudo apt-get update
sudo apt-get install ros-melodic-joint-state-publisher-gui => to install joint_state_publisher_gui
sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control ros-melodic-ros-control ros-melodic-ros-controllers
sudo apt-get install ros-melodic-gazebo-msgs ros-melodic-gazebo-plugins 
sudo apt-get update
sudo apt-get install ros-melodic-rviz-visual-tools
sudo apt-get dist-upgrade
sudo apt-get install ros-melodic-robot-state-publisher
sudo apt-get install ros-melodic-rviz
cd gp_ws
catkin_make
source devel/setup.bash
```
## To run arm in gazebo
```bash
roslaunch arm_gazebo arm_gazebo.launch
```
* **UN-PAUSE SIMULATION FROM GAZEBO GUI**

# Second Terminal
## To add models
```bash
rosrun gazebo_ros spawn_model -database cafe_table -sdf -model cafe_table -y -0 -x -0

rosrun gazebo_ros spawn_model -database coke_can -sdf -model coke_can -reference_frame cafe_table::link -y 0 -x 0.4 -z 0.772

rosrun gazebo_ros spawn_model -database bowl -sdf -model bowl -reference_frame cafe_table::link -y 0.1 -x 0.1 -z 0.775

rosrun gazebo_ros spawn_model -database cricket_ball -sdf -model cricket_ball -reference_frame cafe_table::link -y -0.1 -x 0.2 -z 0.775

rosrun gazebo_ros spawn_model -database hammer -sdf -model hammer -reference_frame cafe_table::link -y -0.1 -x 0.28 -z 0.8
```
## Spawn Camera
```bash
rosrun gazebo_ros spawn_model -file `echo $(rospack find arm_gazebo)`/models/realsense_camera/model.sdf -sdf -model realsense_camera -reference_frame cafe_table::link 
```
## Run Subscriber
```bash
rosrun arm_gazebo subscriber_image.py
```
## To view image data
1. Press Ctrl-T
2. from "gazebo.msgs.ImageStamped" the topic name will be shown
3. Click on the topic name then click "Ok" you will see the camera image data.

# To delete model
1. CLI
```bash
rosservice call gazebo/delete_model '{model_name: realsense_camera}'
```
2. Gazebo GUI: 'Right-click' on the model and click on 'delete'

# To create a launch file for this state 
1. In gazebo gui click on file -> save world as -> write_world_name.world -> save in directory "gp_ws/src/arm_gazebo/worlds/"

2. In MobaXterm go to the directory "gp_ws/src/arm_gazebo/launch/ ", then right click -> new empty file -> your_world_name.launch

3. Copy and past inside launch file :
```xml
<launch>
  <include file="$(find gazebo_ros)/launch/empty_world.launch">
  <!-- We resume the logic in empty_world.launch, changing only the name of the world to be launched -->
    <arg name="world_name" value="$(find arm_gazebo)/worlds/your_world_name.world"/> 
    <arg name="paused" value="false"/>
    <arg name="use_sim_time" value="true"/>
    <arg name="gui" value="true"/>
    <arg name="recording" value="false"/>
    <arg name="debug" value="false"/>
  </include>
</launch>
```

## To start Gazebo simulation GUI with our new world 
```bash
roslaunch arm_gazebo write_world_name.launch
```

# Errors
1. Gazebo [Err] [REST.cc:205] Error in REST request => solution : open this file( ignition/fuel/config.yaml) and replace( url: https://api.ignitionfuel.org) by url: https://api.ignitionrobotics.org

