#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32


def sub_callback(msg):
    print(f"subscribe message : {msg}")

rospy.init_node('unita_sub')

sub = rospy.Subscriber('pub', Int32, sub_callback)

rospy.spin()
# or 
# while not rospy.is_shutdown():
#    pass
