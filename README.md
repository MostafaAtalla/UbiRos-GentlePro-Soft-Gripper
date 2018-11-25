# UbiRos-GentlePro-Soft-Gripper
This is a ROS package for controlling the UbiRos Soft Gripper .

1 - Clone the repository

$ git clone https://github.com/MostafaAtalla/UbiRos-GentlePro-Soft-Gripper.git

2 - Build your catkin_ws

$ cd ~/catkin_ws 
$ catkin_make

3 - Source the workspace so that ROS can find the new package.

$ source devel/setup.bash 

Before step 4, make sure that you have connected the soft gripper to the power supply and the USB port of the computer

4 - There are two ways to launch the control for the soft gripper
  
  A - Through the launch file
  
  $ roslaunch gentlepro_soft_gripper softgripper_launcher.launch
 
  B - Through running the nodes individually
 
  $ roscore
 
  $ rosrun rosserial_python serial_node.py /dev/ttyUSB*
  
  $ rosrun gentlepro_soft_gripper all_fingers_control.py 
  
  You can now use the stated keyboard buttons to control the Ubiros GentlePro soft gripper
