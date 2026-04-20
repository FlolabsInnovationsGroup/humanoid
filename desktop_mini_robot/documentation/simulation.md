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
To mantain reproducibility, the chosen model files saved locally was added to a folder called desk (/models/desk). 

