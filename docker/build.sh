source /opt/ros/melodic/setup.bash
mkdir -p /catkin_ws/src 
cp -r  /data/ceslab_kinect /catkin_ws/src/
cd /catkin_ws 
catkin_make 
source ./devel/setup.bash
chmod +x /catkin_ws/src/ceslab_kinect/scripts/subscriber_image.py



