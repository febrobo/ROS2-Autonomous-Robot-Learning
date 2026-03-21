import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/febin/Desktop/ROS2-Autonomous-Robot-Learning/Project_1_Hello_Node/install/my_robot_pkg'
