import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped
import random
import math

class GPSPublisher(Node):
    def __init__(self):
        super().__init__('gps_publisher')
        self.publisher = self.create_publisher(PointStamped, '/gps/position', 10)

        self.timer = self.create_timer(0.1, self.publish_gps)
        self.time_elapsed = 0.0

    def publish_gps(self):
        msg = PointStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'map'

        self.time_elapsed += 0.1
        msg.point.x = 5.0 * math.cos(0.1 * self.time_elapsed) + random.gauss(0, 0.5)
        msg.point.y = 5.0 * math.sin(0.1 * self.time_elapsed) + random.gauss(0, 0.5)
        msg.point.z = 0.0

        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = GPSPublisher()
    rclpy.spin(node)
    rclpy.shutdown()