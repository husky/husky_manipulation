# Robotiq Gripper on Universal Robots

There are two types of Universal Robot models: Cobots (CB3) and **E-series**. 

If using an **E-series** arm, then using the internal connection is possible; follow the instructions below to setup a Robotiq on a UR E-series arm. 
> If using a **CB3**/**Cobot** arm then the Robotiq gripper will need to be wired directly onto the computer.


## UR Tablet Setup
In **Installation**->**General**->**Tool I/O**:
 - set the tool output voltage to 24V
 - enable **Communication Interface** and use defaults
 - in **General**->**Payload** set the Mass to 1kg
 - save these to the default installation

Add URCap RS485 which will create a socat relay between the arm controller and the computer, such that the computer will be able to access the gripper as if it was connected to it as a USB device. 

Follow these instructions to find how to add the URCap:
 - [Adding a URCap](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/7b6b62bf81f2a032e0b6c7c8e1046cae35e079c7/ur_robot_driver/doc/install_urcap_e_series.md)
 - [Adding the RS485 URCap](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/7b6b62bf81f2a032e0b6c7c8e1046cae35e079c7/ur_robot_driver/doc/setup_tool_communication.md)

## Environment Variable Setup
Use the **setup_husky_ur_envar** script to set and obtain the environment variables required. 

Navigate to the *husky_manipulation/husky_ur_description/scripts/* directory and run the script: `./setup_husky_ur_envar`

See the usage below:
```
Usage: setup_husky_ur_envar -m ARM_MODEL [-d] [-g]
  -h | display this help menu
  -m | [required] arm model: ['ur3', 'ur3e', 'ur5', 'ur5e']
  -d | [optional] add dual arms
  -g | [optional] add gripper to the arm(s)
```
> You must pass `-m` followed by the arm model type: `ur3`, `ur3e`, `ur5`, `ur5e`. \
> Pass `-d` if its a dual arm setup \
> Pass `-g` if the arm(s) have a Robotiq gripper \
> Ex. `./setup_husky_ur_envar -m ur5e -g`, will add a UR5e arm with a Robotiq gripper 
>  - export HUSKY_TOP_PLATE_ENABLED=true
>  - export HUSKY_LARGE_TOP_PLATE=true
>  - export HUSKY_USER_RAIL_ENABLED=false
>  - export HUSKY_UR_GRIPPER_ENABLED=true
>  - export HUSKY_URDF_EXTRAS=/home/lcamero/Workspaces/husky_ws/src/husky_manipulation/husky_ur_description/urdf/husky_ur5_e_description.urdf.xacro

## Description
If a custom URDF already exists, then use `xacro:include` to include the appropriate URDF (i.e. the one added as `HUSKY_URDF_EXTRAS` in the script above)

Ensure that the environment variables are set whenever you run any visualization, whether its `RViz` or the `setup_assistant`

## Bringup
Select either `husky_ur_bringup.launch` or `husky_dual_ur_bringup.launch`.
As long as the `HUKSY_UR_GRIPPER_ENABLED` environment variable is enabled, then the gripper will also be launched. 

## MoveIt Config
Use the script `configure_moveit.sh` in the `husky_ur_robotiq_2f_85_moveit_config` or `husky_dual_ur_robotiq_2f_85_moveit_config` package to create a custom MoveIt! config that includes the gripper by default.