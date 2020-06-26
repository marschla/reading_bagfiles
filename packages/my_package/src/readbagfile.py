#!/usr/bin/env python

import os
import rospy
import rosbag
from duckietown import DTROS
from std_msgs.msg import String
import numpy as np 
import yaml

class MyNode(DTROS):

    def __init__(self, node_name):
        # initialize the DTROS parent class
        super(MyNode, self).__init__(node_name=node_name)

#write data from bagfile to txt file
#bagfile needs to be in correct folder 
#to run prgm correctly, use volume mounting
    def run(self):

        #name of bagfile/txtfile
        #name = "LFdemo2"

        #name from commandline
        name = os.environ['FILENAME']

        rospy.loginfo(name)

        '''
        #choose name of txt file (choose folder according to volume mounting)
        file1 = open("/home/"+name+"_omega.txt","w")
        file2 = open("/home/"+name+"_v.txt","w")
        file3 = open("/home/"+name+"_time.txt","w")
        '''

        #name bag to analyze (attention volume mounting)
        bag = rosbag.Bag('/home/'+name+'.bag')
        #choose topic
        '''
        for topic, msg, t in bag.read_messages("/autobot17/lane_filter_node/lane_pose"):
            #rospy.loginfo(msg)
            file.write(str(msg))
        '''
        
        '''
        arr_omega = []
        arr_v = []
        arr_time = []
        '''

        data = []

        i = 0
        starttime = 0.0

        for topic, msg, t in bag.read_messages("/autobot17/wheels_driver_node/wheels_cmd_decalibrated"):
            #rospy.loginfo(msg.format)
            omega = (msg.vel_left-msg.vel_right)/2.0
            v = (msg.vel_left+msg.vel_right)/2.0
            time = str(msg.header.stamp.secs) + "." + str(msg.header.stamp.nsecs) 
            #rospy.loginfo("omega: %s" % omega)

            if i == 0:
                starttime = float(time)
                #rospy.loginfo("starttime %s" % starttime)
                told = starttime

            '''
            arr_omega.append(omega)
            arr_v.append(v)
            arr_time.append(float(time)-starttime)
            #rospy.loginfo(type(time))
            '''

            tnew = float(time)-starttime
            dt = tnew - told
            #rospy.loginfo("dt: %s" % dt)
            told = tnew

            data_ = {
                "omega" : omega ,
                "v_ref" : v ,
                "time" : float(time)-starttime ,
                "step" : i
            }

            data.append(data_)

            i+=1
        
        '''
        rospy.loginfo(arr_time)
        np.savetxt(file1,arr_omega)
        np.savetxt(file2,arr_v)
        np.savetxt(file3,arr_time)
        file1.close()
        file2.close()
        file3.close()
        '''
        bag.close()

        with open('/home/' + name +'_data.yaml', 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)

        '''
        #choose name of txt file (choose folder according to volume mounting)
        file = open("/home/"+name+"_wd.txt","w")

        #name bag to analyze (attention volume mounting)
        bag = rosbag.Bag('/home/'+name+'.bag')
        #choose topic
        for topic, msg, t in bag.read_messages("/marschla2/wheels_driver_node/wheels_cmd"):
            #rospy.loginfo(msg)
            file.write(str(msg))
        
        bag.close()
        file.close()
        '''






if __name__ == '__main__':
    # create the node
    node = MyNode(node_name='my_node')

    print("Start\n")

    # run node
    node.run()


    print("\nEnd")

    

