#!/usr/bin/env python

import os
import rospy
import rosbag
from duckietown import DTROS
from std_msgs.msg import String
import numpy as np 


class MyNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MyNode, self).__init__(node_name=node_name)

#write data from bagfile to txt file
#bagfile needs to be in correct folder 
#to run prgm correctly, use volume mounting
    def run(self):

        #choose name of txt file (choose folder according to volume mounting)
        file = open("/home/lp1.txt","w")

        #name bag to analyze (attention volume mounting)
        bag = rosbag.Bag('/home/lf2.bag')
        #choose topic
        for topic, msg, t in bag.read_messages("/marschla/lane_filter_node/lane_pose"):
            #rospy.loginfo(msg)
            file.write(str(msg))

        bag.close()
        file.close()


        #choose name of txt file (choose folder according to volume mounting)
        file = open("/home/wd1.txt","w")

        #name bag to analyze (attention volume mounting)
        bag = rosbag.Bag('/home/lf2.bag')
        #choose topic
        for topic, msg, t in bag.read_messages("/marschla/wheels_driver_node/wheels_cmd"):
            #rospy.loginfo(msg)
            file.write(str(msg))

        bag.close()
        file.close()






if __name__ == '__main__':
    # create the node
    node = MyNode(node_name='my_node')

    print("Start\n")

    # run node
    node.run()


    print("\nEnd")

    

