cmake_minimum_required(VERSION 2.8.3)
project(husky_ur_description)

find_package(catkin REQUIRED)

catkin_package()

include_directories()

install(DIRECTORY meshes urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
install(PROGRAMS
scripts/setup_husky_dual_ur3_e_envar
scripts/setup_husky_dual_ur3_envar
scripts/setup_husky_dual_ur5_e_envar
scripts/setup_husky_dual_ur5_envar
scripts/setup_husky_ur3_e_envar
scripts/setup_husky_ur3_envar
scripts/setup_husky_ur5_e_envar
scripts/setup_husky_ur5_envar
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
