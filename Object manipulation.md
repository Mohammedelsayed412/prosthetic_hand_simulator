# Run code

```roslaunch gazebo_ros empty_world.launch```
* In another terminal:
```
   rosrun gazebo_ros spawn_model -database cafe_table -sdf -model cafe_table -y 0 -x -0
   rosrun gazebo_ros spawn_model -database coke_can -sdf -model coke_can -reference_frame cafe_table::link -y 0 -x 0 -z 0.913
   rosrun gazebo_ros spawn_model -database bowl -sdf -model bowl -reference_frame cafe_table::link -y 0 -x 0.2 -z 0.913
   rosrun gazebo_ros spawn_model -database cricket_ball -sdf -model cricket_ball -reference_frame cafe_table::link -y 0 -x -0.1 -z 0.913
   rosrun gazebo_ros spawn_model -database saucepan -sdf -model saucepan -reference_frame cafe_table::link -y 0.1 -x -0.3 -z 0.913
   rosservice call gazebo/delete_model '{model_name: saucepan}'
   rosservice call /gazebo/set_model_state '{model_state: { model_name: coke_can, pose: { position: { x: -0.2, y: 0.2 ,z: 0.913 }, orientation: {x: 0, y: 0.491983115673, z: 0, w: 0.870604813099 } }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , reference_frame: cafe_table } }'
```

# Insert object

1. Make sure that a gazebo world is **already running**, either by:
    * running an empty world:
    ```roslaunch gazebo_ros empty_world.launch```
    * or running any other world:
        * ```
           cd sim_env_ws/src
           source devel/setup.sh
           roslaunch prosthetic_gazebo tables_world.launch
          ```
2. Run commands:
    * **Make sure that model name *-model model_name* isn't repeated**
    * **table**=>```rosrun gazebo_ros spawn_model -database cafe_table -sdf -model cafe_table -y 5 -x -0.3```
    * **To spawn objects relative to table**
    * **coke_can**=>```rosrun gazebo_ros spawn_model -database coke_can -sdf -model coke_can -reference_frame cafe_table::link -y 0 -x 0 -z 0.913```
    * **bowl**=>```rosrun gazebo_ros spawn_model -database bowl -sdf -model bowl -reference_frame cafe_table::link -y 0 -x 0.2 -z 0.913```
    * **cricket ball**=>```rosrun gazebo_ros spawn_model -database cricket_ball -sdf -model cricket_ball -reference_frame cafe_table::link -y 0 -x -0.1 -z 0.913```
    * **saucepan**=>```rosrun gazebo_ros spawn_model -database saucepan -sdf -model saucepan -reference_frame cafe_table::link -y 0 -x 0.2 -z 0.913```
    * For list of available objects:https://bitbucket.org/osrf/gazebo_models/src/default/ or 
http://models.gazebosim.org/

# Delete Object

* To delete saucepan: ```rosservice call gazebo/delete_model '{model_name: saucepan}'```

# Set Model State

* Change position of can: ```rosservice call /gazebo/set_model_state '{model_state: { model_name: coke, pose: { position: { x: -0.2, y: 0.2 ,z: 0.913 }, orientation: {x: 0, y: 0.491983115673, z: 0, w: 0.870604813099 } }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , reference_frame: cafe_table } }'```


# Object manipulation services

* These services allow the user to spawn and destroy models dynamically in simulation:

    * **~/spawn_urdf_model**: gazebo_msgs/SpawnModel - service to spawn a Universal Robotic Description Format (URDF)

    * **~/spawn_sdf_model**: gazebo_msgs/SpawnModel - service to spawn a model written in Gazebo Simulation Description Format (SDF)

    * **~/delete_model**: gazebo_msgs/DeleteModel - service to delete a model from simulation.
* Spawn services:
    * **Insert**
        * Using the service call method with a roslaunch file.http://gazebosim.org/tutorials/?tut=ros_roslaunch
        * From command line:
            * SDF from local model database:
            ```rosrun gazebo_ros spawn_model -file `echo $GAZEBO_MODEL_PATH`/coke_can/model.sdf -sdf -model coke_can1 -y 0.2 -x -0.3 
            ```
            * SDF from the online model database:
            ```rosrun gazebo_ros spawn_model -database coke_can -sdf -model coke_can3 -y 2.2 -x -0.3```
        * ```rosrun gazebo_ros spawn_model -h```=> to see arguments
    * **Delete**
        * ```rosservice call gazebo/delete_model '{model_name: model_name}'```
* State and property:
    * services allow the user to set or get state and property information about simulation and objects in simulation
    * get coke model information: ``` rosservice call gazebo/get_model_state '{model_name: coke}'```
    * get a list of models in the world: ```rosservice call gazebo/get_world_properties```
    * details of a specific model:```rosservice call gazebo/get_model_properties '{model_name: coke}'```
    * Other things we can set: http://gazebosim.org/tutorials/?tut=ros_comm
