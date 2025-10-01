#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node 
from example_interfaces.srv import AddTwoInts 

# Creating a class that inherits from Node
class AddTwoIntsServerNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")

        # Creating a service named "add_two_ints" with the type AddTwoInts
        self.server_= self.create_service(
            AddTwoInts, 'add_two_ints', self.callback_add_two_ints)
        self.get_logger().info("AddTwoInts server is ready.")
    
    # Callback function that will be called whenever a request is received
    def callback_add_two_ints(self, request:AddTwoInts.Request, response:AddTwoInts.Response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum))
        return response
    
def main(args=None):
        rclpy.init(args = args)
        node = AddTwoIntsServerNode()
        try:
            rclpy.spin(node)
        except KeyboardInterrupt:
             pass 
        finally:
            node.destroy_node()
            rclpy.shutdown()

if __name__ == "__main__":
        main()
