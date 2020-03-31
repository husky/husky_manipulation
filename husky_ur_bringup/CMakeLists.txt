cmake_minimum_required(VERSION 2.8.3)
project(husky_ur_bringup)

find_package(catkin REQUIRED COMPONENTS)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch/husky_ur_official_bringup.launch)
  roslaunch_add_file_check(launch/husky_dual_ur_official_bringup.launch)
  roslaunch_add_file_check(launch/husky_ur_modern_bringup.launch)
  roslaunch_add_file_check(launch/husky_dual_ur_modern_bringup.launch)
endif()

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS
  scripts/arm_reset.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
