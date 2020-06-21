# Must install
```bash
sudo apt-get update
sudo apt-get install ros-melodic-joint-state-publisher-gui => to install joint_state_publisher_gui
sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control ros-melodic-ros-control ros-melodic-ros-controllers
sudo apt-get install ros-melodic-gazebo-msgs ros-melodic-gazebo-plugins 

```
# Commands
```bash
cd sim_env_ws
catkin_make
source devel/setup.bash
```
## To run arm in Rviz with GUI joint controllers
```bash
roslaunch prosthetic_gazebo arm_rviz.launch
```
## To run arm in gazebo
```bash
roslaunch prosthetic_gazebo arm_gazebo.launch
roslaunch arm_control arm_control.launch
```
* **UN-PAUSE SIMULATION FROM GAZEBO GUI**

```bash
rostopic pub -1 /arm_stand/joint_mid_top_position_controller/command std_msgs/Float64 "data: 1.57"
rostopic pub -1 /arm_stand/joint_base_mid_position_controller/command std_msgs/Float64 "data: 1.57"
rostopic pub -1 /arm_stand/joint_top_fore_position_controller/command std_msgs/Float64 "data: 1.57"

```
# To check parsing of urdf file and look at links/joints tree
```bash
cd "sim_env_ws/src/arm_description/urdf/"
rosrun xacro xacro arm_stand.urdf.xacro > arm_stand.urdf
check_urdf "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/src/arm_description/urdf/arm_stand.urdf"
urdf_to_graphiz arm_stand.urdf 
```  
# Changes in tiago_robot/tiago_description/urdf/end_effector/end_effector.urdf.xacro:
```xml
<!-- Hand -->
  <xacro:if value="${type == 'pal-hey5'}">
    <xacro:hey5_hand parent="${parent}" name="${name}" reflect="${reflect}">
      <origin xyz="${height3} 0 0" rpy="-1.57 0 0"/>
      <!--<origin xyz="0 0 0" rpy="0 0 0"/>-->
    </xacro:hey5_hand>

    <joint name="${name}_safety_box_joint" type="fixed">
      <parent link="${parent}"/>
      <child link="${name}_safety_box"/>
      <origin xyz="${height3} 0 0" rpy="-1.57 0 0"/>
      <!--<origin xyz="0.1 0.02 ${reflect * 0.02}" rpy="0 0 0"/>-->
    </joint>
```
# Changes in "src/tiago_description_complete/hey5_description/urdf/actuators.urdf.xacro" 
```xml
<!-- Position joint reducer -->
  <xacro:macro name="position_reducer" params="name reduction" >
    <transmission name="${name}_trans">
      <type>transmission_interface/SimpleTransmission</type>
      <actuator name="${name}_motor" >
        <mechanicalReduction>${reduction}</mechanicalReduction>
      </actuator>
      <joint name="${name}_joint" >
        <!--<hardwareInterface>hardware_interface/PositionJointInterface</hardwareInterface>-->
        <hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
      </joint>
    </transmission>
  </xacro:macro>
```
for no PositionJointInterface. Other soltn: adding pid in .yaml file: (didnt do that one)
```yaml
/gazebo_ros_control:   
  pid_gains:
    shoulder_pan_joint: <!--Joints with error-->
      p: 100.0
      i: 0.01 
      d: 10.0
```

