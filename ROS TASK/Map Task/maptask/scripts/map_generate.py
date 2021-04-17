#!/usr/bin/env python

from __future__ import print_function
import rospy

from maptask.srv import map_from_image,map_from_imageResponse


def handle_center(req):
    center = [req.centerX , req.centerY]
    return map_from_imageResponse([req.centerX,req.centerY])

def map_generate_server():
    rospy.init_node('map_generate_server')
    s = rospy.Service('map_generate',map_from_image,handle_center)
    print("Server Running")
    rospy.spin()

if __name__ == "__main__":
    map_generate_server()


