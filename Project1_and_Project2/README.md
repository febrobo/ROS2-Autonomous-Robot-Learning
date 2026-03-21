# Projects 1 & 2: Foundations — Nodes, Publishers & Topics

## Overview

These two projects form the foundation of ROS2. Project 1 teaches what a node is and how to keep it alive. Project 2 teaches how nodes **broadcast data** to the rest of the robot system using topics. Together they answer the most fundamental ROS2 question: *"How do nodes talk to each other?"*

---

## Project 1: Your First Node — Hello Robotics

### What I Built

A ROS2 node called `hello_robot` that:
- Initializes itself as a ROS2 node
- Creates a timer that triggers every 1 second
- Prints a "Heartbeat" message with an incrementing counter
- Keeps running until stopped with `Ctrl+C`

### How to Run

```bash
source /opt/ros/humble/setup.bash
cd ROS2-Autonomous-Robot-Learning/Project_1_2_Foundations
colcon build --packages-select my_robot_pkg
source install/setup.bash
ros2 run my_robot_pkg hello_node
```

### Expected Output
```
[INFO] [hello_robot]: Hello Robotics World! Node is alive.
[INFO] [hello_robot]: Heartbeat #1
[INFO] [hello_robot]: Heartbeat #2
[INFO] [hello_robot]: Heartbeat #3
...
```

### What I Learned Line by Line

```python
import rclpy                    # Core ROS2 Python library
from rclpy.node import Node    # Base class for all nodes
```

```python
class HelloRobot(Node):                          # Inherit from Node
    def __init__(self):
        super().__init__('hello_robot')          # Register node name with ROS2
        self.timer = self.create_timer(1.0, self.timer_callback)  # Fire every 1s
        self.count = 0
```

```python
def timer_callback(self):
    self.count += 1
    self.get_logger().info(f'Heartbeat #{self.count}')  # ROS2 logging (not print!)
```

```python
rclpy.init()          # Initialize ROS2
node = HelloRobot()   # Create the node
rclpy.spin(node)      # Keep alive — wait for callbacks to fire
rclpy.shutdown()      # Clean exit
```

### Key Concepts
- **Nodes**: The basic building block of ROS2. Everything is a node.
- **Timers & Callbacks**: `create_timer(interval, function)` fires a function repeatedly
- **rclpy.spin()**: Keeps the node alive. Without it, the node starts and immediately exits
- **Logging**: Use `get_logger().info()` instead of `print()` — ROS2 can filter, timestamp, and route logs

### Verify the Node is Running
```bash
# In another terminal
ros2 node list
# Output: /hello_robot

ros2 node info /hello_robot
# Shows: publishers, subscribers, services attached to this node
```

---

## Project 2: Publisher — Streaming Fake Sensor Data

### What I Built

A ROS2 publisher node called `gps_publisher` that:
- Creates a publisher on the `/gps/position` topic
- Publishes `PointStamped` messages at **10 Hz** (every 0.1 seconds)
- Simulates a robot moving in a **circle of radius 5 meters**
- Adds **Gaussian noise** (std dev = 0.5m) to mimic real GPS inaccuracy
- Stamps each message with a timestamp and coordinate frame

### How to Run

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run my_robot_pkg gps_publisher
```

The terminal goes silent — that's normal! The node is publishing, not printing. Open other terminals to observe it.

### Verifying It Works (4 Terminal Setup)

**Terminal 1 — Run the node (keep this running):**
```bash
source /opt/ros/humble/setup.bash && source install/setup.bash
ros2 run my_robot_pkg gps_publisher
```

**Terminal 2 — Check topic exists:**
```bash
ros2 topic list
# Output:
# /gps/position
# /parameter_events
# /rosout
```

**Terminal 3 — See live data streaming:**
```bash
ros2 topic echo /gps/position
# Output:
# header:
#   stamp:
#     sec: 1774113827
#     nanosec: 323710848
#   frame_id: map
# point:
#   x: 5.232702670006204
#   y: -0.08086456588715007
#   z: 0.0
```

**Terminal 4 — Verify publish rate:**
```bash
ros2 topic hz /gps/position
# Output:
# average rate: 10.000
#   min: 0.099s max: 0.101s std dev: 0.00017s window: 136
```

### New Message Type: PointStamped
```
geometry_msgs/PointStamped
├── header
│   ├── stamp      ← when was this reading taken?
│   └── frame_id   ← relative to which coordinate frame? ("map")
└── point
    ├── x          ← meters
    ├── y          ← meters
    └── z          ← 0.0 for a 2D robot
```

### What I Learned Line by Line

```python
from geometry_msgs.msg import PointStamped  # Standard ROS2 position+timestamp message
import random                                # For GPS noise
import math                                  # For sin/cos circle motion
```

```python
self.publisher = self.create_publisher(PointStamped, '/gps/position', 10)
#                                       ^^^^^^^^^^^   ^^^^^^^^^^^^^^  ^^
#                                       msg type      topic name      queue size
```

```python
self.timer = self.create_timer(0.1, self.publish_gps)
#                               ^^^
#                               0.1 seconds = 10 Hz
```

```python
msg = PointStamped()
msg.header.stamp = self.get_clock().now().to_msg()      # Timestamp this reading
msg.header.frame_id = 'map'                             # Coordinates relative to map
self.time_elapsed += 0.1
msg.point.x = 5.0 * math.cos(0.1 * self.time_elapsed) + random.gauss(0, 0.5)
msg.point.y = 5.0 * math.sin(0.1 * self.time_elapsed) + random.gauss(0, 0.5)
msg.point.z = 0.0
self.publisher.publish(msg)                             # BROADCAST to all subscribers
```

### Why the Numbers Look Noisy
The robot traces a circle of radius 5m. `random.gauss(0, 0.5)` adds ±0.5m noise every publish. So x is never exactly 5.0 — you'll see `4.87`, `5.23`, `5.31`. This is exactly how a real GPS behaves.

### setup.py Entry Points
```python
entry_points={
    'console_scripts': [
        'hello_node = my_robot_pkg.hello_node:main',
        'gps_publisher = my_robot_pkg.gps_publisher:main',  # ← added for Project 2
    ],
},
```

---

## Topics — The Big Picture

```
TOPICS ARE LIKE RADIO CHANNELS:

Publisher (broadcast tower)         Subscriber (radio)
      │                                    │
      │   /gps/position topic              │
      └──────────────────────────────────► │
                                           │
                              Any number of subscribers
                              can tune into the same topic.
                              Publisher doesn't know or care.
```

| Property | Behavior |
|---|---|
| Direction | One way: publisher → subscriber |
| Subscribers | Any number can listen simultaneously |
| Publisher awareness | Publisher does NOT know who is listening |
| Data | Latest message only — no guarantee of delivery |

### Topics vs Services vs Actions

| Type | Pattern | Use When |
|---|---|---|
| **Topics** | Publish → Subscribe | Continuous streaming (sensors, state) |
| **Services** (Project 5) | Request → Response | One-time operations (calibrate, save map) |
| **Actions** (Project 6) | Goal → Feedback → Result | Long tasks with progress (navigate to point) |

---

## Project Structure

```
Project_1_2_Foundations/
├── src/my_robot_pkg/
│   ├── my_robot_pkg/
│   │   ├── __init__.py           (Python package marker)
│   │   ├── hello_node.py         (Project 1 — heartbeat node)
│   │   └── gps_publisher.py      (Project 2 — GPS publisher node)
│   ├── package.xml               (Package metadata)
│   ├── setup.py                  (Entry points for both executables)
│   ├── setup.cfg                 (Package configuration)
│   └── resource/
└── output/
    └── project_output.txt        (Terminal output from both projects)
```

---

## Common Mistakes & Fixes

### "ros2: command not found"
```bash
source /opt/ros/humble/setup.bash   # Must do this in every new terminal
# Or add to ~/.bashrc to make it permanent:
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

### Topic list only shows /parameter_events and /rosout
The publisher node isn't running! A topic **only exists while a publisher is active**. Start the node first, then check.

### New terminal doesn't see your package
```bash
source install/setup.bash   # Required in every new terminal after building
```

---

## CLI Commands Reference

```bash
# Nodes
ros2 node list                   # All running nodes
ros2 node info /node_name        # Publishers, subscribers, services of a node

# Topics
ros2 topic list                  # All active topics
ros2 topic echo /topic_name      # Print live messages
ros2 topic hz /topic_name        # Measure actual publish rate
ros2 topic info /topic_name      # Message type + publisher/subscriber count
```

---

## Time Spent

| Task | Time |
|---|---|
| Project 1 — workspace setup & first node | ~65 min |
| Project 2 — publisher & topic debugging | ~60 min |
| **Total** | **~125 min** |

---

## Next Steps

Project 3 introduces **Subscribers** — a `gps_monitor` node that tunes into `/gps/position` and computes running statistics (average position every 5 seconds). The publisher from Project 2 keeps running **completely unchanged**. The subscriber just tunes in. That's the beauty of pub/sub.

---

## References
- [ROS2 Humble Official Docs](https://docs.ros.org/en/humble/)
- [geometry_msgs/PointStamped](https://docs.ros2.org/humble/api/geometry_msgs/msg/PointStamped.html)
- [The Robotics Back-End](https://theroboticsbackend.com/)
- [Articulated Robotics YouTube](https://www.youtube.com/@ArticulatedRobotics)

---

**Created by:** Febin  
**Started:** March 7, 2026  
**Completed:** March 21, 2026  
**Status:** ✅ Both Complete
