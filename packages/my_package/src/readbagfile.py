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
        file = open("/home/lf2.txt","w")

        #name bag to analyze (attention volume mounting)
        bag = rosbag.Bag('/home/lf2.bag')
        #choose topic
        for topic, msg, t in bag.read_messages("/marschla/lane_filter_node/lane_pose"):
            rospy.loginfo(msg)
            file.write(str(msg))

        bag.close()
        file.close()

#currently unused
def extract():
    dist = []
    phi = []

    with open('/home/lf2.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
        
            #only using specific lines 
            if line[0]+line[1]=="d:":
                dist.append(float(line[2:]))
                #print(float(line[2:]), end='')
                #print("\n")
            if line[0]+line[1]+line[2]+line[3] == "phi:":
                phi.append(float(line[4:]))

            #next line
            line = reader.readline()





if __name__ == '__main__':
    # create the node
    node = MyNode(node_name='my_node')

    print("Start\n")

    # run node
    node.run()

    #do not uncomment, does not work properly/no real functionality yet
    #extract()

    print("\nEnd")

    

