# Robot
## To launch tiago robot
1. Run commands from inside sim_env_ws:
```shell
catkin_make
source devel/setup.sh
```
2. To launch tiago with our simple world at specific gzpose in relation to our table:
```shell
roslaunch prosthetic_gazebo sim_env.launch gzpose:='-x -1.9 -y -1.9 -z 0.0 -R 0.0 -P 0.0 -Y 0.0'
```
3. To launch tiago in a custom world:
    1. Create your custom world file with objects. Or modify *startup_world.world* (our basic world) file by launching: `roslaunch prosthetic_gazebo no_robot_world.launch
` and spawning or deleting objects then saving the new world configuration as a new .world file.
    2. Change world file in *sim_env.launch* launch file to your new .world file.
    3. Then run `roslaunch prosthetic_gazebo sim_env.launch gzpose:='-x -1.9 -y -1.9 -z 0.0 -R 0.0 -P 0.0 -Y 0.0'`

## To insert your own robot
1. Find your ROBOT_DESCRIPTION package. 
2. Download this package and place it inside the sim_env_ws inside a new folder ROBOT_DESCRIPTION_ALL.
3. Find the packag.xml file and download any other package needed by ROBOT_DESCRIPTION package and also place them inside the folder ROBOT_DESCRIPTION_ALL. 
4. run commands from inside sim_env_ws:
```shell
catkin_make
source devel/setup.sh
```
5. Navigate to the sim_env_ws launch folder and open *sim_env.launch* file. Run commands from inside prosthetic_simulation: 
```bash
cd sim_env_ws/src/prosthetic_gazebo/launch
nano sim_env.launch
```
6. Inside launch file **change** the following parts: 
    1. The robot launch file arguments depending on any arguments required by your robot's **MAIN** xarco or urdf description file. The gzpose defines initial position of robot.
    2. The robot description tags **param** and **rosparam**: Inside **param**: `$(find tiago_description)/robots/tiago.urdf.xacro` change package name to ROBOT_DESCRIPTION and the path `/robots/tiago.urdf.xacro` to the one that includes your robot's **MAIN** xarco or urdf description file and change the name of arg tags according to those in point **a**. Inside **rosparam**: change package and file name to the collision.yaml file of your robot if it exists.
    3. Spawn robot inside gazebo change -model name instead of tiago to your robot name.
    ```xml
    <launch>
    ...
    <!--Robot launch files arguments-->
      <arg name="arm"  default="True"/>
      <arg name="end_effector"  default="pal-hey5"/>
      <arg name="ft_sensor"  default="schunk-ft"/>
      <arg name="laser_model"  default="false"/>
      <arg name="camera_model"  default="orbbec-astra"/>
      <arg name="wrist_model"  default="wrist-2017"/>
      <arg name="multi" default=""/>
      <arg name="gzpose" default="-x -0.9 -y -0.9 -z 0.0 -R 0.0 -P 0.0 -Y 0.0"/>

      <!-- Robot description -->
      <param name="robot_description"
        command="rosrun xacro xacro '$(find tiago_description)/robots/tiago.urdf.xacro'
        arm:=$(arg arm)
        wrist_model:=$(arg wrist_model)
        end_effector:=$(arg end_effector)
        ft_sensor:=$(arg ft_sensor)
        laser_model:=$(arg laser_model)
        camera_model:=$(arg camera_model)
        $(arg multi)" />

      <rosparam command="load" file="$(find tiago_description)/config/collision/collision_parameters.yaml" />

      <!-- Spawn a robot into Gazebo -->
      <node name="spawn_urdf" pkg="gazebo_ros" type="spawn_model" args="-urdf -param robot_description $(arg gzpose) -reference_frame cafe_table::link -model tiago" />

    </launch>
    ```

