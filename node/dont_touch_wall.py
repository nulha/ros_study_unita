#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

rospy.init_node("dont_touch_wall")

pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(5)


min = -2
max = 2


def sub_callback(pose):
    go = Twist()
    if pose.x < 0.8 or pose.x > 10.2 or pose.y< 0.8 or pose.y > 10.2 :
        go.linear.x = 1
        go.angular.z = 2
    else :
        go.linear.x = random.uniform(1,3)
        go.angular.z = random.uniform(min,max)
    pub.publish(go)


dtw_sub = rospy.Subscriber('turtle1/pose', Pose, sub_callback)



while not rospy.is_shutdown():
    rate.sleep()
    
