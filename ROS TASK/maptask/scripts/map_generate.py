#!/usr/bin/env python

from __future__ import print_function
import rospy

from map_from_image.srv import(centerX,centerY)


def handle_center(req):
    center = [req.centerX,req.centerY]
    return center

def map_generate_server():
    rospy.init_node('map_generate_server')
    s = rospy.Service('map_generate',map_from_image,handle_center)
    rospy.spin()

if __name__ == "__main__":
    map_generate_server()


