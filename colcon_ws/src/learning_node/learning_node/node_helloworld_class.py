#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node
import time

# capsule the node functions into a class
class HelloWorldNode(Node):
    def __init__(self, name, freqT):
        self.count = 0
        self.freqT = freqT

        super().__init__(name)  # inherit from the parent class
        while rclpy.ok():
            self.get_logger().info("[msg NO.%04d] Hello world!"%self.count)
            time.sleep(self.freqT)  # set the freq from the outside
            self.count += 1

def main(args=None):
    rclpy.init(args=args)

    # instantiate a node object: (node_name, freqT)
    node = HelloWorldNode("node_helloworld_oop", 0.5)
        # it would be better that node name the same as .py name
        # but not necessary
    
    node.destroy_node()
    rclpy.shutdown()
