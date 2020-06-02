# Install script for directory: /home/ceslab/prosthetic_hand_simulator/sim_env_ws/src/tiago_robot/tiago_description

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/build/tiago_robot/tiago_description/catkin_generated/installspace/tiago_description.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tiago_description/cmake" TYPE FILE FILES
    "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/build/tiago_robot/tiago_description/catkin_generated/installspace/tiago_descriptionConfig.cmake"
    "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/build/tiago_robot/tiago_description/catkin_generated/installspace/tiago_descriptionConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tiago_description" TYPE FILE FILES "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/src/tiago_robot/tiago_description/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tiago_description/gazebo" TYPE DIRECTORY FILES "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/src/tiago_robot/tiago_description/gazebo/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tiago_description/Media" TYPE DIRECTORY FILES "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/src/tiago_robot/tiago_description/Media/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tiago_description/meshes" TYPE DIRECTORY FILES "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/src/tiago_robot/tiago_description/meshes/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tiago_description/robots" TYPE DIRECTORY FILES "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/src/tiago_robot/tiago_description/robots/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tiago_description/urdf" TYPE DIRECTORY FILES "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/src/tiago_robot/tiago_description/urdf/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tiago_description/config" TYPE DIRECTORY FILES "/home/ceslab/prosthetic_hand_simulator/sim_env_ws/src/tiago_robot/tiago_description/config/")
endif()

