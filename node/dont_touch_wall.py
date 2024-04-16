#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import random

rospy.init_node("dont_touch_wall")

pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(5)

angular_speed = None

def update_angular_speed():
    new_value = random.uniform(3, 3.5)
    return new_value if random.choice([True, False]) else -new_value


def sub_callback(pose):
    global angular_speed 
    go = Twist()
    if pose.x < 1 or pose.x > 10 or pose.y< 1 or pose.y > 10 :
        go.linear.x = 1.8
        if angular_speed is None:
            angular_speed = update_angular_speed()
        go.angular.z = angular_speed
    else :
        go.linear.x = random.uniform(1,3)
        go.angular.z = random.uniform(-3,3)
        angular_speed = None
    pub.publish(go)


dtw_sub = rospy.Subscriber('turtle1/pose', Pose, sub_callback)



while not rospy.is_shutdown():
    rate.sleep()
    