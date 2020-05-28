#! /bin/bash 
source /opt/ros/melodic/setup.bash 
nohup roslaunch gazebo_ros empty_world.launch gui:=false gzweb:=true verbose:=true &>/dev/null & 
sleep 10 
nohup rosrun gazebo_ros spawn_model -file /data/kinect/model.sdf -sdf -x 0 -y 0 -z 0 -R 0 -P 0 -Y 0 -model kinect_ros &>/dev/null & 
sleep 10
cd ~/gzweb
npm start
