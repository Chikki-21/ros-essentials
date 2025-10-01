#!usr/bin/env python3
import rclpy 
from rclpy.node import Node 
from example_interfaces.msg import String

# Creating a class that inherits from Node
class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__('robot_news_station')
        self.declare_parameter("robot_name","R2D2")
        self.robot_name = self.get_parameter("robot_name").value

        # declaring a parameter with a default value of 1.0 seconds
        self.declare_parameter("timer_period", 1.0)  
        self.timer_period_ = self.get_parameter("timer_period").value 

        # Creating a publisher to publish String messages on the "robot_news" topic
        self.publisher_= self.create_publisher(String,"robot_news", 10) 
        self.get_logger().info("Robot News Station Node has been started.")
    
    # Setting up a timer to call the publish_news function periodically
    def publish_news(self):
        msg = String()
        msg.data = f"Hello from {self.robot_name}"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()



