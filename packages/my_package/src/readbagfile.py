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

    def run(self):

        file = open("/home/movement.txt","w")

        bag = rosbag.Bag('/home/bag2.bag')
        for topic, msg, t in bag.read_messages("/marschla/lane_filter_node/lane_pose"):
            rospy.loginfo(msg)
            file.write(str(msg))

        bag.close()
        file.close()

def extract():
    dist = []
    phi = []

    with open('/home/test.txt', 'r') as reader:
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

    print("Commence operation Order 66!")

    # run node
    node.run()

    #print("We secured the Jedi Archives!")

    #extract()

    print("Order 66 executed, all Jedis are dead!")

    

