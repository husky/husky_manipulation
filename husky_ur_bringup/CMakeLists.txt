cmake_minimum_required(VERSION 2.8.3)
project(husky_ur_bringup)

find_package(catkin REQUIRED COMPONENTS
  tf2_ros
  ur_modern_driver
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch/husky_ur_bringup.launch)
  roslaunch_add_file_check(launch/husky_dual_ur_bringup.launch)
endif()
