# Insert, delete and modify objects 

```
    roslaunch gazebo_ros empty_world.launch
    rosrun gazebo_ros spawn_model -database cafe_table -sdf -model cafe_table -y 0 -x -0
    rosrun gazebo_ros spawn_model -database coke_can -sdf -model coke_can -reference_frame cafe_table::link -y 0 -x 0 -z 0.913
    rosrun gazebo_ros spawn_model -database bowl -sdf -model bowl -reference_frame cafe_table::link -y 0 -x 0.2 -z 0.913
    rosrun gazebo_ros spawn_model -database cricket_ball -sdf -model cricket_ball -reference_frame cafe_table::link -y 0 -x -0.1 -z 0.913
    rosrun gazebo_ros spawn_model -database saucepan -sdf -model saucepan -reference_frame cafe_table::link -y 0.1 -x -0.3 -z 0.913
    rosservice call gazebo/delete_model '{model_name: saucepan}'
    rosservice call /gazebo/set_model_state '{model_state: { model_name: coke_can, pose: { position: { x: -0.2, y: 0.2 ,z: 0.913 }, orientation: {x: 0, y: 0.491983115673, z: 0, w: 0.870604813099 } }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , reference_frame: cafe_table } }'
```
## Launch arm_stand

```
roslaunch prosthetic_gazebo arm_gazebo.launch
rosrun gazebo_ros spawn_model -file `echo $(rospack find prosthetic_gazebo)`/models/camera/Camera_model.sdf -sdf -model camera -y 0 -x -0.4 -z 0.913
% Open window topic visualization
rosservice call gazebo/delete_model '{model_name: camera}'
```

## Arm_control

### Rviz
close gazebo
```
roslaunch arm_moveit_config demo.launch %open planning and play 
rosrun prosthetic_gazebo move_group_python_interface.py %pinch
rosrun moveit_commander moveit_commander_cmdline.py
use hand
go relaxed_hand
quit

```

### Gazebo

1. Control using rqt_joint_controller_gui:
```shell
rosrun rqt_joint_trajectory_controller rqt_joint_trajectory_controller
```
2. Control using moveit and rviz gui
```shell 
roslaunch arm_control arm_moveit_control_rviz.launch
```
3. Control using script and change the group name or target pose in script
```shell
roslaunch arm_control arm_moveit_control.launch
rosrun prosthetic_gazebo move_group_python_interface.py % change it
```
4. Control using keyboard: hand{'p':"pinch", 't':"tripod", 'n':"neutral", 'r':"relaxed_hand", 'o':"pronated"},arm{ 'h':"home"}:
```shell
rosrun prosthetic_gazebo move_group_py.py
rosrun prosthetic_gazebo keyboard_publisher.py
```