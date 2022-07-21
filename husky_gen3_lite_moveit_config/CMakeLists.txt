cmake_minimum_required(VERSION 3.1.3)
project(husky_gen3_lite_moveit_config)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(PROGRAMS
  scripts/customize_moveit.sh
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
