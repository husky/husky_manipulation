cmake_minimum_required(VERSION 2.8.3)
project(husky_kinova_bringup)

find_package(catkin REQUIRED COMPONENTS)

catkin_package()

if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch/husky_dual_gen3_bringup.launch)
  roslaunch_add_file_check(launch/husky_gen3_bringup.launch)
  roslaunch_add_file_check(launch/husky_gen3_lite_bringup.launch)
endif()

include_directories(
  ${catkin_INCLUDE_DIRS}
)
