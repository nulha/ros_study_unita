#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('pub')
pub = rospy.Publisher('pub', Int32, queue_size=10)

rate = rospy.Rate(5)

count = 1

while not rospy.is_shutdown():
    rospy.loginfo(f"loginfo :  {count}")
    print(f"print : {count}")
    pub.publish(count)
    count = count + 1
    rate.sleep()
