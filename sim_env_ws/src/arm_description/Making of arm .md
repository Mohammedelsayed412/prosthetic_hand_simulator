# Must install
```bash
sudo apt-get install ros-melodic-joint-state-publisher-gui => to install joint_state_publisher_gui
```
# Changes in tiago_description/urdf/end_effector/end_effector.urdf.xacro:
```xml
<!-- Hand -->
  <xacro:if value="${type == 'pal-hey5'}">
    <xacro:hey5_hand parent="${parent}" name="${name}" reflect="${reflect}">
      <origin xyz="0 0 ${height2 - axle_offset}" rpy="0 -1.57 0"/>
      <!--<origin xyz="0 0 0" rpy="0 0 0"/>-->
    </xacro:hey5_hand>

    <joint name="${name}_safety_box_joint" type="fixed">
      <parent link="${parent}"/>
      <child link="${name}_safety_box"/>
      <origin xyz="0 0 ${height2 - axle_offset}" rpy="0 -1.57 0"/>
      <!--<origin xyz="0.1 0.02 ${reflect * 0.02}" rpy="0 0 0"/>-->
    </joint>
```
# To check parsing of urdf file and look at links/joints tree
```bash
cd "sim_env_ws/src/arm_description/urdf/"
rosrun xacro xacro arm_stand.urdf.xacro > arm_stand.urdf
check_urdf "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/src/arm_description/urdf/arm_stand.urdf"
urdf_to_graphiz arm_stand.urdf 
```  
