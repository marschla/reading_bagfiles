#!/usr/bin/env python
import numpy as np
#import matplotlib.pyplot as plt

#name of txt file
name = "PID1_4"


#basic filter (if this even counts as filter)
def filter(arr):
    arrf = np.arange(0,len(arr),dtype = np.float64)
    for i in range(0,len(arr)):
        if i!=0 and i!=len(arr)-1:
            arrf[i] = (arr[i-1]+arr[i]+arr[i+1])/3.0
        if i==0:
            arrf[i] = (arr[i]+arr[i]+arr[i+1])/3.0
        if i==len(arr)-1:
            arrf[i] = (arr[i-1]+arr[i]+arr[i])/3.0
            
        #print(arrf[i])
        
    return arrf

#sets first timeinstant to zero and puts other timestamps relativ to first one
def reltime(arr):
    arrf = np.arange(0,len(arr),dtype = np.float64)
    t0 = arr[0]
    for i in range(0,len(arr)):
        if i==0:
            arrf[i]=0
        else:
            arrf[i]=arr[i]-t0
    
    return arrf


#arrays where data is stored for plot
dist = []
phi = []
in_lane = []
time_pose = []
v_l = []
v_r = []
time_vel = []


#txt file to analyze
with open('/home/marco/bagfiles/'+name+'_lp.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        
        #only using specific lines 

        #extracting d
        if line[0]+line[1]=="d:":
            dist.append(float(line[2:]))

        #extracting phi
        if line[0]+line[1]+line[2]+line[3] == "phi:":
            phi.append(float(line[4:]))
        
        #extracting in_lane
        if line[0]+line[1] == "in":
            if line[9]=="T":
                in_lane.append(1)
                #print(line[9])
            else:
                in_lane.append(0)
                #print(line[9])

        if line[4]+line[5]+line[6] == "sec":
            nline = reader.readline()
            t = float(line[10:])+float(nline[11:])/1000000000.0
            time_pose.append(t)
    
        #next line
        line = reader.readline()

'''
with open('/home/marco/bagfiles/'+name+'_wd.txt','r') as reader:
    line = reader.readline()
    while line != "":
        #extracting velocities (->actuator inputs)
        if line[0]+line[1]+line[2]+line[3]+line[4] == "vel_l":
            nline = reader.readline()
            v_l.append(float(line[10:]))
            
            #becaue after v_r there is a "header" too, this part figures out the length of the number
            j=0
            for i in nline[11:]:
                if i!="0" and i!="1" and i!="2" and i!="3" and i!="4" and i!="5" and i!="6" and i!="7" and i!="8" and i!="9" and i!="." and i!="-":
                    break
                j+=1
            #print(nline[11:11+j])
            v_r.append(float(nline[11:11+j]))

        if line[4]+line[5]+line[6] == "sec":
            nline = reader.readline()
            t = float(line[10:])+float(nline[11:])/1000000000.0
            time_vel.append(t)
        line = reader.readline()

#the last element in the v_r/v_l element are the stop commands, which are not really interesting -> remove
v_r.pop(len(v_r)-1)
v_l.pop(len(v_l)-1)
time_vel.pop(len(time_vel)-1)
'''
#comment if data should not be filtered
#distf = filter(dist)

#time = reltime(time)
  
print("\nData extracted")
'''
#computing velocity difference, since this our main control input
vdif = np.arange(0,len(v_l),dtype = float)
for i in range(0,len(v_l)):
    vdif[i]=v_r[i]-v_l[i]
'''

'''
#plots
xaxis1 = np.arange(0,len(dist))
plt.scatter(xaxis1,dist,color='red',label="distance to lane center",s=5.0)
plt.title("lane_pose data")
plt.legend()
#plt.show()
#plt.scatter(xaxis1,phi)
#plt.show()
plt.show()

xaxis2 = np.arange(0,len(v_l))
plt.scatter(xaxis2,v_l,color='red',label='vel_left',s=5.0)
plt.scatter(xaxis2,v_r,color='green',label='vel_right',s=5.0)
plt.legend()
plt.title("wheels_cmd data")
plt.show()
'''


#writing data to txt file for further use 
'''
file = open("/home/marco/estimatedelay/data1_dist.txt","w")
file.write(str(dist))
file.close()

file = open("/home/marco/estimatedelay/data1_phi.txt","w")
file.write(str(phi))
file.close()

file = open("/home/marco/estimatedelay/data1_vdif.txt","w")
file.write(str(vdif))
file.close()

file = open("/home/marco/estimatedelay/data1_timepose.txt","w")
file.write(str(time_pose))
file.close()

file = open("/home/marco/estimatedelay/data1_timevel.txt","w")
file.write(str(time_vel))
file.close()
'''

#using numpy to store an array of floats seems to be more convenient
np.savetxt("/home/marco/data_eval/"+name+"_dist.txt",dist)
np.savetxt("/home/marco/data_eval/"+name+"_phi.txt",phi)
#np.savetxt("/home/marco/data_eval/"+name+"_vdif.txt",vdif)
np.savetxt("/home/marco/data_eval/"+name+"_timepose.txt",time_pose)
#np.savetxt("/home/marco/data_eval/"+name+"_timevel.txt",time_vel)
np.savetxt("/home/marco/data_eval/"+name+"_in_lane.txt",in_lane)

print("\nData stored.")