# ROS2 Autonomous Robot Learning — Complete 25 Project Curriculum

## About This Repository

This repository documents my complete learning journey through ROS2, from basic node creation to building a fully autonomous robot system. I'm following a structured curriculum of 25 projects, each building on the previous one.

The philosophy: **ROS2 is not a language—it's a framework for making robots talk to each other.**

## Learning Path

```
LEVEL 1: FOUNDATIONS — "Nodes That Talk"
├── Project 1: Your First Node
├── Project 2: Publisher — Streaming Sensor Data
├── Project 3: Subscriber — Listening to Data
├── Project 4: Custom Messages
├── Project 5: Services — Request/Response
├── Project 6: Actions — Long-Running Tasks
└── Project 7: Launch Files

LEVEL 2: TRANSFORMS & VISUALIZATION
├── Project 8: TF2 Transforms
├── Project 9: URDF Robot Description
└── Project 10: RViz2 Markers

LEVEL 3: SIMULATION
├── Project 11: Gazebo Simulation
└── Project 12: Sensor Processing Nodes

LEVEL 4: ARCHITECTURE
├── Project 13: Quality of Service (QoS)
├── Project 14: Lifecycle Nodes
└── Project 15: Component Composition

LEVEL 5: NAVIGATION
├── Project 16: SLAM Map Building
├── Project 17: AMCL Localization
├── Project 18: Full Nav2 Stack
├── Project 19: Waypoint Navigation
└── Project 20: Costmaps & Behavior Trees

LEVEL 6: CONTROL & HARDWARE
├── Project 21: ros2_control
└── Project 22: Sensor Fusion EKF

LEVEL 7: PRODUCTION & ADVANCED
├── Project 23: rosbag2 Recording
├── Project 24: Custom Nav2 Plugin
└── Project 25: COMPLETE AUTONOMOUS ROBOT
```

## What Each Level Teaches

### **LEVEL 1: FOUNDATIONS** — Understanding ROS2 Communication
The first 7 projects teach how ROS2 nodes communicate:
- **Topics**: One-way streaming (pub/sub)
- **Services**: Request/response calls
- **Actions**: Long-running tasks with feedback
- **Launch Files**: Starting multiple nodes together

By Project 7, I'll understand how to build systems where nodes work together.

### **LEVEL 2: TRANSFORMS & VISUALIZATION** — Where is Everything?
Projects 8-10 teach spatial relationships:
- **TF2**: Tracking coordinate frames on the robot
- **URDF**: Describing the robot's physical structure
- **RViz2**: Visualizing everything in 3D

I'll be able to answer: "Where is the camera relative to the base?"

### **LEVEL 3: SIMULATION** — Virtual Robot Lab
Projects 11-12 introduce Gazebo simulation:
- Full physics simulation
- Simulated sensors (LiDAR, camera, IMU)
- Testing code without real hardware

By Project 12, I'll process real sensor data (from simulation).

### **LEVEL 4: ARCHITECTURE** — Production-Ready Code
Projects 13-15 teach best practices:
- **QoS**: How to configure message delivery guarantees
- **Lifecycle Nodes**: Safe startup/shutdown sequences
- **Component Composition**: Running multiple nodes in one process for speed

I'll understand how production robots are structured.

### **LEVEL 5: NAVIGATION** — Autonomous Movement
Projects 16-20 teach the complete navigation stack:
- **SLAM**: Building maps from sensor data
- **Localization**: Finding the robot on the map
- **Nav2**: Full autonomous navigation system
- **Waypoints**: Multi-goal missions
- **Tuning**: Customizing behavior for different environments

By Project 20, my robot will navigate autonomously.

### **LEVEL 6: CONTROL & HARDWARE** — Making Things Move
Projects 21-22 teach:
- **ros2_control**: Standard hardware abstraction for motors/actuators
- **Sensor Fusion**: Combining multiple sensors (my own EKF algorithm)

I'll integrate my Robotics curriculum algorithms into ROS2.

### **LEVEL 7: PRODUCTION & ADVANCED** — Putting It All Together
Projects 23-25 teach real-world skills:
- **rosbag2**: Recording and replaying robot data for testing
- **Plugins**: Extending Nav2 with custom algorithms
- **Capstone**: Building a complete autonomous system

Project 25 is the ultimate demo: a robot that explores, maps, navigates, detects objects, and reports status.

## Connection to Other Curricula

This ROS2 curriculum integrates with my other learning:

| My Algorithm | ROS2 Implementation |
|---|---|
| Kalman Filter (Robotics) | EKF as ROS2 Node (Project 22) |
| Particle Filter (Robotics) | AMCL in Nav2 (Project 17) |
| A* Path Planning (Robotics) | Custom Nav2 Plugin (Project 24) |
| DWA Local Planner (Robotics) | DWB Controller in Nav2 (Project 18) |
| YOLO Detection (CUDA) | Camera Processing Node (Project 12) |
| Point Cloud Processing (CUDA) | LiDAR Processing Node (Project 12) |

## Project Structure

Each project folder contains:

```
Project_N_ProjectName/
├── README.md              (Detailed writeup for this project)
├── src/                   (ROS2 workspace with package)
│   └── my_package/
│       ├── my_package/    (Python code)
│       ├── package.xml
│       ├── setup.py
│       └── setup.cfg
└── output/                (Screenshots, logs, results)
    └── project_output.txt (Terminal output from running)
```

## Getting Started

### Prerequisites
- Ubuntu 22.04 LTS
- ROS2 Humble installed: https://docs.ros.org/en/humble/Installation.html
- `colcon` build tool: `sudo apt install python3-colcon-common-extensions`

### For Each Project
1. Navigate to the project folder: `cd Project_1_Hello_Node`
2. Follow the README.md in that folder
3. Build: `colcon build --packages-select my_package`
4. Source: `source install/setup.bash`
5. Run: `ros2 run my_package executable_name`

## Essential ROS2 Commands I'm Learning

```bash
# Node management
ros2 node list                          # See all running nodes
ros2 node info /node_name               # Details about a node

# Topic debugging
ros2 topic list                         # All active topics
ros2 topic echo /topic_name             # Print messages from a topic
ros2 topic hz /topic_name               # Measure publish rate

# Service calls
ros2 service list                       # All available services
ros2 service call /service_name Type    # Call a service

# Parameter management
ros2 param list /node_name              # Node parameters
ros2 param set /node_name param value   # Set a parameter

# Building and running
colcon build                            # Build all packages
colcon build --packages-select pkg      # Build specific package
source install/setup.bash               # Activate workspace

# Visualization
rviz2                                   # Launch RViz2 visualizer
```

## Progress Tracking

| Project | Title | Status | Date | Notes |
|---------|-------|--------|------|-------|
| 1 | Hello Node | ✅ Complete | Mar 7, 2026 | Basic node with timer |
| 2 | Publisher | ✅ Complete | Mar 21, 2026 | GPS publisher node, 10Hz, PointStamped msg |
| 3 | Subscriber | ⏳ Planned | - | Data processing |
| 4 | Custom Messages | ⏳ Planned | - | Robot state message |
| 5 | Services | ⏳ Planned | - | Calibration service |
| 6 | Actions | ⏳ Planned | - | Movement with feedback |
| 7 | Launch Files | ⏳ Planned | - | Multi-node startup |
| 8-10 | Transforms & Viz | ⏳ Planned | - | TF2, URDF, RViz2 |
| 11-12 | Simulation | ⏳ Planned | - | Gazebo + sensors |
| 13-15 | Architecture | ⏳ Planned | - | QoS, Lifecycle, Components |
| 16-20 | Navigation | ⏳ Planned | - | SLAM, Nav2 stack |
| 21-22 | Control | ⏳ Planned | - | ros2_control, EKF |
| 23-25 | Production | ⏳ Planned | - | rosbag2, plugins, capstone |

## Key Insights

### What I'm Learning
1. **ROS2 is modular**: Everything is a plugin or a node
2. **Reusability**: The same code works on simulation and real robots
3. **Abstraction**: `tf2`, `ros2_control`, and `nav2` hide complexity
4. **Debugging**: ROS2 CLI tools are incredibly powerful

### Common Mistakes to Avoid
- Forgetting to `source install/setup.bash` after building
- QoS mismatches between publishers and subscribers (silent failure!)
- Not using lifecycle nodes for complex startup sequences
- Not recording rosbags during development

## Resources I'm Using

### Official Documentation
- [ROS2 Humble Docs](https://docs.ros.org/en/humble/)
- [Nav2 Documentation](https://navigation.ros.org/)
- [ROS2 Design Articles](https://design.ros2.org/)

### Learning Resources
- [The Robotics Back-End](https://theroboticsbackend.com/) — Best tutorials
- [Articulated Robotics](https://www.youtube.com/@ArticulatedRobotics) — Full robot series
- [Steve Macenski](https://www.youtube.com/@SteveMacenski) — Nav2 deep dives

### Tools
- **RViz2**: 3D visualization of robot state
- **Gazebo**: Physics simulation
- **tf2_tools**: Visualize coordinate frame trees
- **rosbag2**: Record and replay sensor data

## Philosophy

> "The best way to learn ROS2 is not to read docs—it's to build systems."

Each project builds something **working** that I can actually run. By Project 25, I'll have built a complete autonomous robot system and understand every layer of it.

## Goals

✅ **Short term** (Projects 1-7): Understand ROS2 communication  
✅ **Medium term** (Projects 8-15): Build visualization and simulation skills  
🎯 **Long term** (Projects 16-25): Deploy a fully autonomous robot  
🚀 **Interview ready**: "I built 25 ROS2 projects and understand the entire stack"

## Contributing

This is my personal learning journey, but I'm open to:
- Suggestions for additional projects
- Better ways to structure the code
- Improvements to documentation

## License

MIT License — feel free to learn from these projects!

---

## Next Steps

I'm currently on **Project 2**. Next is **Project 3: Subscriber**, where I'll build a node that listens to the GPS data and computes statistics.

Follow along as I work through the complete curriculum. Each project folder will have detailed documentation, working code, and actual output from running the system.

---

**Learning Since:** March 7, 2026  
**Current Status:** Building Block 1/7 ✅  
**GitHub:** [@febrobo](https://github.com/febrobo)
