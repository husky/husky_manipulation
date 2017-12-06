cmake_minimum_required(VERSION 2.8.3)
project(husky_ur_bringup)

find_package(catkin REQUIRED COMPONENTS
  ur_bringup
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES husky_ur_bringup
#  CATKIN_DEPENDS ur_bringup
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch/husky_dual_ur_bringup.launch launch/husky_ur_bringup.launch)
endif()
