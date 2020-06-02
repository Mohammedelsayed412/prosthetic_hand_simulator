# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;std_msgs;controller_manager;control_toolbox;pluginlib;hardware_interface;transmission_interface;joint_limits_interface;urdf;angles;gazebo_ros_control".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lrobot_hw_sim_latency".split(';') if "-lrobot_hw_sim_latency" != "" else []
PROJECT_NAME = "robot_hw_sim_latency"
PROJECT_SPACE_DIR = "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/install"
PROJECT_VERSION = "0.0.1"
