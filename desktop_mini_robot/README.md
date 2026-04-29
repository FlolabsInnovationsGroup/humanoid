# Desktop Mini Robot
The Desktop Mini Robot is a mini autonomous robot that combines hardware with a virtual assistant using the FloBrain. 

## ROS 2
The embedded software utilizes ROS (Robot Operational System) 2 to control the robot. 

To install all the dependencies, run the following commands in the root folder:
```
colcon build --symlink-install
source install/setup.bash
```

To create the ROS 2 workspace the following command was used: 

```
ros2 pkg create --build-type ament_cmake ros_workspace
```


