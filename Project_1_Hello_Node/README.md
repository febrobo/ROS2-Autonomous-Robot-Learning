# Project 1: Your First Node — Hello Robotics

## Overview

This is my first step into ROS2. I learned how to create a ROS2 workspace, build a package, and write my first node that prints heartbeat messages at regular intervals. The goal was to understand the basics of ROS2 structure and how nodes work.

## What I Built

A simple ROS2 node called `hello_robot` that:
- Initializes itself as a ROS2 node
- Creates a timer that triggers every 1 second
- Prints a "Heartbeat" message with an incrementing counter
- Keeps running until I stop it with `Ctrl+C`

## Key Learnings

### ROS2 Fundamentals
- **Nodes**: The basic building blocks in ROS2. Everything is a node.
- **Workspace**: The folder structure where all ROS2 projects live (`src/`, `build/`, `install/`, `log/`)
- **Packages**: Collections of ROS2 code organized in a specific structure
- **rclpy**: The Python library that lets you write ROS2 nodes

### Code Concepts
- **Timers & Callbacks**: Using `create_timer()` to trigger functions at fixed rates
- **Node Class**: Inheriting from `Node` to create a ROS2 node
- **Logging**: Using `get_logger().info()` instead of print statements
- **Entry Points**: Configuring `setup.py` so ROS2 knows how to run your executable

### ROS2 CLI Commands
I learned these debugging commands:
- `ros2 node list` — See all running nodes
- `ros2 node info /node_name` — Get details about a specific node
- `ros2 pkg list` — List all packages in your workspace

## Project Structure

```
Project_1_Hello_Node/
├── src/my_robot_pkg/
│   ├── my_robot_pkg/
│   │   ├── __init__.py           (Python package marker)
│   │   └── hello_node.py         (The actual ROS2 node)
│   ├── package.xml               (Package metadata)
│   ├── setup.py                  (Entry points for executables)
│   ├── setup.cfg                 (Package configuration)
│   └── resource/                 (Package resources)
└── output/
    └── project_1_output.txt      (Console output from running the node)
```

## How to Run

### Prerequisites
- ROS2 Humble installed on Ubuntu 22.04
- `colcon` build system installed

### Step 1: Source ROS2
```bash
source /opt/ros/humble/setup.bash
```

### Step 2: Navigate to Workspace
```bash
cd ROS2-Autonomous-Robot-Learning/Project_1_Hello_Node
```

### Step 3: Build the Package
```bash
colcon build --packages-select my_robot_pkg
```

### Step 4: Source the Build
```bash
source install/setup.bash
```

### Step 5: Run the Node
```bash
ros2 run my_robot_pkg hello_node
```

### Expected Output
```
[INFO] [hello_robot]: Hello Robotics World! Node is alive.
[INFO] [hello_robot]: Heartbeat #1
[INFO] [hello_robot]: Heartbeat #2
[INFO] [hello_robot]: Heartbeat #3
[INFO] [hello_robot]: Heartbeat #4
[INFO] [hello_robot]: Heartbeat #5
...
```

The counter increments every second until you press `Ctrl+C` to stop the node.

## Verify the Node is Running

In another terminal, source and run:

```bash
source install/setup.bash
ros2 node list
```

You should see:
```
/hello_robot
```

Get more details:
```bash
ros2 node info /hello_robot
```

Output:
```
/hello_robot
  Subscribers:

  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
  Service Servers:
    /hello_robot/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /hello_robot/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /hello_robot/get_parameters: rcl_interfaces/srv/GetParameters
    /hello_robot/list_parameters: rcl_interfaces/srv/ListParameters
    /hello_robot/set_parameters: rcl_interfaces/srv/SetParameters
    /hello_robot/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:

  Action Clients:
```

## What I Learned Line by Line

### Imports
```python
import rclpy                    # Core ROS2 library
from rclpy.node import Node    # Base class for all nodes
```

### Node Class
```python
class HelloRobot(Node):         # Inherit from Node to create a ROS2 node
    def __init__(self):
        super().__init__('hello_robot')  # Initialize parent with node name
```

### Timer & Callback
```python
self.timer = self.create_timer(1.0, self.timer_callback)  # Fire callback every 1 second
self.count = 0                  # Counter for heartbeat number
```

### The Callback Function
```python
def timer_callback(self):
    self.count += 1             # Increment counter
    self.get_logger().info(f'Heartbeat #{self.count}')  # Log with counter value
```

### Main Entry Point
```python
rclpy.init()                    # Initialize ROS2
node = HelloRobot()             # Create node instance
rclpy.spin(node)                # Keep node alive and processing callbacks
rclpy.shutdown()                # Clean shutdown
```

## Time Spent
- Learning ROS2 basics: ~20 minutes
- Setting up workspace & package: ~15 minutes
- Writing and debugging code: ~20 minutes
- Testing and verification: ~10 minutes
- **Total: ~65 minutes**

## Next Steps
Project 2 will introduce **Publishers** — I'll create a node that simulates a GPS sensor and publishes position data continuously. That's when things get really interesting because two nodes will communicate with each other!

## Reference
- [ROS2 Humble Official Docs](https://docs.ros.org/en/humble/)
- [The Robotics Back-End](https://theroboticsbackend.com/)
- [Articulated Robotics YouTube Series](https://www.youtube.com/@ArticulatedRobotics)

---

**Created by:** Febin  
**Date:** March 7, 2026  
**Status:** ✅ Complete
