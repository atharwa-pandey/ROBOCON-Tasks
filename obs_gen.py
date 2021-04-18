#!/usr/bin/env python

import rospy
from std_msgs.msg import list

rospy.init_node('obstacle_gen', anonymous=True)


pub = rospy.Publisher('obstacle',list , queue_size=1)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    for i in range(1,4):
        for j in range(0,4):
            center.append([1.5*i , 1.5*j])
    publisher.publish(center)
    rate.sleep()
