# Run commands


`cd sim_env_ws`

`catkin_make`

`echo "source devel/setup.bash" >> ~/.bashrc`

`chmod +x src/prosthetic_gazebo/scripts/subscriber_image.py`

## Run launch file

`
roslaunch prosthetic_gazebo sim_env.launch
`

## Spawn kinect and run subscriber

```
rosrun gazebo_ros spawn_model -file `echo $(rospack find prosthetic_gazebo)`/models/kinect/model.sdf -sdf -model kinect -y 0 -x -0.5 -z 0.913
```

`rosrun prosthetic_gazebo subscriber_image.py`


## Spawn camera

```
rosrun gazebo_ros spawn_model -file `echo $(rospack find prosthetic_gazebo)`/models/camera/Camera_model.sdf -sdf -model camera -y 0 -x -0.8 -z 0.913
```

## Insert, delete and modify objects 

* Close gazebo then
* ```
    roslaunch gazebo_ros empty_world.launch
    rosrun gazebo_ros spawn_model -database cafe_table -sdf -model cafe_table -y 0 -x -0
    rosrun gazebo_ros spawn_model -database coke_can -sdf -model coke_can -reference_frame cafe_table::link -y 0 -x 0 -z 0.913
    rosrun gazebo_ros spawn_model -database bowl -sdf -model bowl -reference_frame cafe_table::link -y 0 -x 0.2 -z 0.913
    rosrun gazebo_ros spawn_model -database cricket_ball -sdf -model cricket_ball -reference_frame cafe_table::link -y 0 -x -0.1 -z 0.913
    rosrun gazebo_ros spawn_model -database saucepan -sdf -model saucepan -reference_frame cafe_table::link -y 0.1 -x -0.3 -z 0.913
    rosservice call gazebo/delete_model '{model_name: saucepan}'
    rosservice call /gazebo/set_model_state '{model_state: { model_name: coke_can, pose: { position: { x: -0.2, y: 0.2 ,z: 0.913 }, orientation: {x: 0, y: 0.491983115673, z: 0, w: 0.870604813099 } }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , reference_frame: cafe_table } }'
```
