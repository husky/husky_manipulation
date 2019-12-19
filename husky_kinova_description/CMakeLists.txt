cmake_minimum_required(VERSION 2.8.3)
project(husky_kinova_description)

find_package(catkin REQUIRED COMPONENTS)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(DIRECTORY urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS
  scripts/setup_husky_gen3_envar
  scripts/setup_husky_gen3_robotiq_2f_85_envar
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
