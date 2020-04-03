#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

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
lane = []
time = []
v_l = []
v_r = []

#txt file to analyze
with open('/home/marco/bagfiles/lp_wd_2.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        
        #only using specific lines 

        #extracting d
        if line[0]+line[1]=="d:":
            dist.append(float(line[2:]))
            #print(float(line[2:]), end='')
            #print("\n")

        #extracting phi
        if line[0]+line[1]+line[2]+line[3] == "phi:":
            phi.append(float(line[4:]))
        
        #extracting in_lane
        if line[0]+line[1] == "in":
            if line[9]=="T":
                lane.append(1)
                #print(line[9])
            else:
                lane.append(0)
                #print(line[9])

        #extracting velocities (->actuator inputs)
        if line[0]+line[1]+line[2]+line[3]+line[4] == "vel_l":
            nline = reader.readline()
            v_l.append(float(line[10:]))
            
            #becaue after v_r there is a "header" too, this part figures out the length of the number
            j=0
            for i in nline[11:]:
                if i!="0" and i!="1" and i!="2" and i!="3" and i!="4" and i!="5" and i!="6" and i!="7" and i!="8" and i!="9" and i!=".":
                    break
                j+=1
            #print(nline[11:11+j])
            v_r.append(float(nline[11:11+j]))
            
            
        
        #next line
        line = reader.readline()

#the last element in the v_r/v_l element are the stop commands, which are not really interesting -> remove
v_r.pop(len(v_r)-1)
v_l.pop(len(v_l)-1)

#comment if data should not be filtered
distf = filter(dist)

#time = reltime(time)
  
print("\nData extracted")

#plots
xaxis1 = np.arange(0,len(dist))
plt.scatter(xaxis1,dist,color='red',label="not filtered",s=5.0)
#plt.scatter(time,distf,color='green',label="filtered",s=5.0)
plt.legend()
#plt.show()
#plt.scatter(xaxis1,phi)
#plt.show()
#plt.scatter(xaxis1,lane)
plt.show()


#computing velocity difference, since this our main control input
vdif = np.arange(0,len(v_l),dtype = float)
for i in range(0,len(v_l)):
    vdif[i]=v_r[i]-v_l[i]

xaxis2 = np.arange(0,len(v_l))
plt.scatter(xaxis2,v_l,color='red',label='vel_left',s=5.0)
plt.scatter(xaxis2,v_r,color='green',label='vel_right',s=5.0)
plt.legend()
plt.show()



