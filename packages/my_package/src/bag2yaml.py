#!/usr/bin/env python3

import os
import rospy
import rosbag
from duckietown.dtros import DTROS, NodeType
from std_msgs.msg import String
import numpy as np 
import yaml

class MyNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MyNode, self).__init__(node_name=node_name,node_type=NodeType.GENERIC)

#write data from bagfile to txt file
#bagfile needs to be in correct folder 
#to run prgm correctly, use volume mounting
    def run(self):

        #name from commandline
        name = os.environ['FILENAME']
        #name = "test1"

        rospy.loginfo(name)

        #name bag to analyze (attention volume mounting)
        bag = rosbag.Bag('/home/'+name+'.bag')
        #choose topic

        data = []

        i = 0
        starttime = 0.0

        first_msg_rec = False

        for topic, msg, t in bag.read_messages("/fakebot/sim_node/global_pose"):

            rospy.loginfo(msg.header.stamp.nsecs)

            pos_x = msg.x 
            pos_y = msg.y 
            pos_theta = msg.theta

            time = float(msg.header.stamp.secs) + float(msg.header.stamp.nsecs)/1e9

            if first_msg_rec == False:
                starttime = time
                first_msg_rec = True

            data_ = {
                "pos_x" : pos_x ,
                "pos_y" : pos_y,
                "theta" : pos_theta ,
                "time_stamp" : time-starttime
            }

            data.append(data_)

            i+=1
        

        bag.close()

        with open('/home/' + name +'_data.yaml', 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)


if __name__ == '__main__':
    # create the node
    node = MyNode(node_name='my_node')

    print("Start\n")

    # run node
    node.run()


    print("\nEnd")

    

