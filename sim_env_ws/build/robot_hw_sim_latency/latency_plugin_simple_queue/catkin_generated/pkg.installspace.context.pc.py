# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;pluginlib;robot_hw_sim_latency".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-llatency_plugin_simple_queue".split(';') if "-llatency_plugin_simple_queue" != "" else []
PROJECT_NAME = "latency_plugin_simple_queue"
PROJECT_SPACE_DIR = "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/install"
PROJECT_VERSION = "0.0.1"
