#!/usr/bin/env python
import rospy
import math
from jamkit.msg import sensor_raw
from std_msgs.msg import Float64
pub_j21 = rospy.Publisher('j2_1_controller',Float64, queue_size=10)
pub_j22 = rospy.Publisher('j2_2_controller',Float64, queue_size=10)

##About:

##Authors: Ahmed Sami Deiri


def split(goalangle):
    print("Node: j2_controller")

    pub_j21.publish(goalangle)
    joint2angle = 3.14159 - goalangle
    pub_j22.publish(joint2angle)
    return()

def listener():  #subscribes to topic, calls function split() when a message is published on topic.
    rospy.init_node('j2_controller', anonymous=True)
    rospy.Subscriber("state", Float64, split)  ##subscribes to topic hand_sensing_output. Expects a float array with 27 values.

    rospy.spin()


if __name__ == '__main__':
    print("Running")
    listener()
