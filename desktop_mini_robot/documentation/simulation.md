# Simulation

 This document explains how the simulation was first created, what its components are, and how you can run it on your computer.

**TOPICS:**

1. Simulation workspace components
2. How to run the simulation
3. Creation of the simulation workspace

## 1. Simulation workspace components

First of all, the simulator used is [Gazebo](https://gazebosim.org/home). 

## 3. Creation of the simulation workspace

The simulation workspace was first created on Gazebo Harmonic in Ubuntu 22 OS.

### Simulation world

The simulation world came from the [Gazebo Open Models](https://app.gazebosim.org/fuel/models).

The goal of the simulation world is to emulate the desk environment that the robot will move on. For that, the [desk model](https://app.gazebosim.org/OpenRobotics/fuel/models/Office%20Desk) was chosen to be the world model.

After choosing the model, it was opened on the simulator by running:

```

gz sim --verbose 3

```

Followed by creating an empty project, opening the Resource Spawner, searching by Office Desk, downloading the resource and adding it to the world simulation. 


Once chosen the model to be used, the world was saved as a SDF (Simulation Description Format) file.