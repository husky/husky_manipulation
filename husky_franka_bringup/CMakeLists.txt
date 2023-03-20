cmake_minimum_required(VERSION 3.4)
project(husky_franka_bringup)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(catkin REQUIRED COMPONENTS
  franka_control
  franka_hw
  franka_msgs
)

catkin_package(
  CATKIN_DEPENDS
    franka_control
    franka_hw
    franka_msgs
  DEPENDS Franka
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
