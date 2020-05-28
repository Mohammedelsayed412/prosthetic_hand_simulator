# Run launch file

```
cd sim_env_ws
source devel/setup.sh
roslaunch prosthetic_gazebo sim_env.launch

```
* **Image of what appears**:  [Image](sim_env.png)

# roslaunch command

* **roslaunch** => starts ROS nodes
* **Format** =>
```
    roslaunch ros_package package_launch_file
```
* To launch empty world
```
    roslaunch gazebo_ros empty_world.launch
```
* **Arguments**=>
    * **paused** => Start Gazebo in a paused state (default false)
    * **use_sim_time** => Tells ROS nodes asking for time to get the Gazebo-published simulation time, published over the ROS topic /clock (default true)
    * **gui** => Launch the user interface window of Gazebo (default true)
    * **recording** => Enable gazebo state log recording
    * **debug** => Start gzserver (Gazebo Server) in debug mode using gdb (default false)
    * **verbose** => Run gzserver and gzclient with --verbose, printing errors and warnings to the terminal (default false)
* **Example** =>
```
    roslaunch gazebo_ros empty_world.launch paused:=true use_sim_time:=false gui:=true throttled:=false recording:=false debug:=true verbose:=true
```

# launch file

```
<launch>
  <arg name="gui" default="true"/>
  <arg name="start_gazebo" default="true"/>
  <arg name="limited" default="false"/>
  <arg name="paused" default="false"/>
  <arg name="gzweb" default="false"/>
  <arg name="verbose" default="false"/>
  <!-- We resume the logic in empty_world.launch, changing only the name of the world to be launched -->
  <include file="$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="world_name" value="$(find YOUR_PACKAGE_NAME)/worlds/YOUR_WORLD_NAME.world"/> 
    <arg name="paused" value="false"/>
    <arg name="use_sim_time" value="true"/>
    <arg name="gui" value="true"/>
    <arg name="recording" value="false"/>
    <arg name="debug" value="false"/>
  </include>
  
</launch>
```

* This is a typical launch file that specifies the world to be launched.
* Specify package that you already have on your system and the name of the world you want to launch

# To use roslaunch

* A .launch file must be found in a launch folder inside a working ROS package made using catkin_create_pkg PACKAGE_NAME command.
* It specfies the .world to be run which should be found in a worlds folder in a valid ROS package.
* For more info regarding spawning (robot, controllers, models) using launch file:
    * http://gazebosim.org/tutorials/?tut=ros_roslaunch
    * Book: Carol Fairchild, ROS robotics by example
    * Book: Wyatt Newman, A systematic approach to learning robot programming with ROS
