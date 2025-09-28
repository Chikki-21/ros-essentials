#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from example_interfaces.msg import String

# Creating a class that inherits from Node
class RobotNewsSubscriberNode(Node):
    def __init__(self):
        super().__init__("robot_news_subscriber")

        # Creating a subscriber to listen to String messages on the "robot_news" topic
        self.subscriber_= self.create_subscription(String, "robot_news", self.callback_robot_news, 10)
        self.get_logger().info("Robot News Subscriber Node has been started.")
        
    # callback function that will be called whenever a new message is received on the "robot_news" topic
    def callback_robot_news(self, msg:String):
        self.get_logger().info("Message received :"+ msg.data)

    
def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
