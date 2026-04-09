#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    # 初始化节点
    rospy.init_node('talker', anonymous=True)
    
    # 创建一个发布者对象
    pub = rospy.Publisher('chatter', String, queue_size=10)
    
    # 设置发布频率
    rate = rospy.Rate(10) # 10 Hz
    
    while not rospy.is_shutdown():
        # 创建一个消息
        hello_str = "hello world %s" % rospy.get_time()
        
        # 打印消息到控制台
        rospy.loginfo(hello_str)
        
        # 发布消息
        pub.publish(hello_str)
        
        # 等待直到下一个周期
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
