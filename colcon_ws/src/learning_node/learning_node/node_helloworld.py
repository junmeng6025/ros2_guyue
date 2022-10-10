#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
import time

def main(args=None):
    rclpy.init(args=args)
    node = Node("node_helloworld")
    count = 0

    while rclpy.ok():
        node.get_logger().info("[msg NO.%04d]Hello world!"%count)
        time.sleep(0.5)  # set the T=0.5s, i.e. freq=2Hz
        count += 1

    node.destroy_node()
    rclpy.shutdown()
