#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 

# Creating a class that inherits from Node
class MyFirstNode(Node):
    def __init__(self):
        super().__init__("py_node")
        self.get_logger().info("Hello, ROS2 from Python!")

        # Setting up a timer to call a function every second
        self.timer = self.create_timer(1.0, self.timer_callback)

        # The timer will call the timer_callback function every 1 second
    def timer_callback(self):
        self.get_logger().info("Timer callback executed.")

# Main function to initialize and run the node
def main(args=None):
    rclpy.init(args=args)
    node = MyFirstNode()
    node.get_logger().info("Node has been started successfully.")
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
