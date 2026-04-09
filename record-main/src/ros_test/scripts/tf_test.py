#!/usr/bin/env python

import rospy
import tf
import tf.transformations as tft
from geometry_msgs.msg import TransformStamped
import numpy as np

def broadcaster():
    rospy.init_node('tf_broadcaster')

    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)

    while not rospy.is_shutdown():
        # Define the transformation (e.g., translation and rotation)
        translation = (1.0, 2.0, 3.0)  # (x, y, z)
        quaternion = tf.transformations.quaternion_from_euler(0, 0, np.pi/4)  # Roll, Pitch, Yaw

        # Send the transformation from parent frame to child frame
        br.sendTransform(translation,
                         quaternion,
                         rospy.Time.now(),
                         "child_frame",
                         "parent_frame")
        rate.sleep()

if __name__ == '__main__':
    try:
        broadcaster()
    except rospy.ROSInterruptException:
        pass
