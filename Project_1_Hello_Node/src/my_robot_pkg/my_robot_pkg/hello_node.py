import rclpy
from rclpy.node import Node

class HelloRobot(Node):
    def __init__(self):
        super().__init__('hello_robot')
        self.get_logger().info('Hello Robotics World! Node is alive.')
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        self.count += 1
        self.get_logger().info(f'Heartbeat #{self.count}')

def main():
    rclpy.init()
    node = HelloRobot()
    rclpy.spin(node)
    rclpy.shutdown()