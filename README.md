# 6DOFRobotRosTrajectoryPlaning
This is a ROS project in where we design a 6DOF robot URDF and visualize its motion on RVIZ and simulate it on GAZEBO

You need to install ROS Neotic and its packages:
http://wiki.ros.org/noetic/Installation
You need to install all gazebo packages :
https://classic.gazebosim.org/tutorials?tut=ros_installing&cat=connect_ros
You need to install Moveit:
https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html

I made this project on Ubuntu WSL and used Xlaunch for GUI:
https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview
https://seanthegeek.net/234/graphical-linux-applications-bash-ubuntu-windows/

To run the package RVIZ and Gazebo together use the next command:
roslaunch YrbN5ls demo_gazebo.launch 

Don't forget after closing to avoid error in opening it again use the next command:
killall gzserver && killall gzclient && killall rviz && killall rosmaster
