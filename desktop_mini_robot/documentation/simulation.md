# Simulation

 This document explains how the simulation was first created, what its components are, and how you can run it on your computer.

**TOPICS:**

1. Simulation workspace components
2. How to run the simulation
3. Creation of the simulation workspace

## 1. Simulation workspace components

First of all, the simulator used is [Gazebo](https://gazebosim.org/home). The simulation is breaken down into world and robot.

## 2. How to run the simulation

After instaling all the ROS workspace dependencies (as shown in the project's README.md file), in the root folder execute the following command to run the simulation on Gazebo by ROS:
```
ros2 launch ros_workspace simulation_launch.py
```

## 3. Creation of the simulation workspace

The simulation workspace was first created on Gazebo Harmonic in Ubuntu 22 OS. After creating the world, the ROS 2 workspace was created to smoothly launch the simulation with all simulation models integrated and to prepare for the future development.

### Simulation world

The simulation world came from the [Gazebo Open Models](https://app.gazebosim.org/fuel/models).

The goal of the simulation world is to emulate the desk environment that the robot will move on. For that, the [desk model](https://app.gazebosim.org/OpenRobotics/fuel/models/Office%20Desk) was chosen to be the world model.

<img width="488" height="392" alt="image" src="https://github.com/user-attachments/assets/9e100116-7a2a-4c85-b230-ddf4a43844a2" />


After choosing the model, it was opened on the simulator by running:

```

gz sim --verbose 3

```

Followed by creating an empty project, opening the Resource Spawner, searching by Office Desk, downloading the resource and adding it to the world simulation. 

Once chosen the model to be used, the world was saved as a SDF (Simulation Description Format) file.  
To maintain reproducibility, the chosen model files saved locally was added to a folder called desk (/models/desk). 

### Simulation robot

At first, the goal to simulate the robot is to test the embedded software. For that, there is no need to create a realistic robot model. The model created focus on the main components of the robot: wheels, infrared sensor, simplified body. Later, a fully detailed 3D design will replace our simple model.

The simplistic model contains four wheels, a base to connect the wheels, the infrared sensor and a rectangle box above it representing the body. 

To simulate the model, a URDF file was created with all the representations needed to apply the design. To add the model to the simulation world, a model.config file was created with the reference to the urdf file that will be read by Gazebo. 

To view only the robot created, the rViz tool was used. For that a launch file was created and it is used by running 
```
ros2 launch ros_workspace robot_rviz_view_launch.py
```

