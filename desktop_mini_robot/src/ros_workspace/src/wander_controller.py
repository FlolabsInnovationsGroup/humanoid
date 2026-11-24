#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WanderController(Node):
    def __init__(self):
        super().__init__('wander_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        self.subscription = self.create_subscription(
            LaserScan,
            '/ir_sensor/scan',
            self.sensor_callback,
            10)
        
        self.get_logger().info('Wander Controller has been started. Moving forward.')
        self.move_forward()

    def sensor_callback(self, msg):
        if msg.ranges:
            distance = msg.ranges[0]
            if(distance > 0.1):
                self.stop()
                self.get_logger().info(f'Edge detected')
            else:
                self.move_forward()

    def move_forward(self):
        msg = Twist()
        msg.linear.x = 0.1
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
    
    def stop(self):
        msg = Twist()
        msg.linear.x = 0.0
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
