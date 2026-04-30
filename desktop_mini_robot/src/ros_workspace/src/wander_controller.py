#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class WanderController(Node):
    def __init__(self):
        super().__init__('wander_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Wander Controller has been started. Moving forward.')

    def timer_callback(self):
        msg = Twist()
        # Move forward at 0.5 m/s
        msg.linear.x = 0.5
        # No rotation
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    wander_controller = WanderController()

    try:
        rclpy.spin(wander_controller)
    except KeyboardInterrupt:
        pass

    wander_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
