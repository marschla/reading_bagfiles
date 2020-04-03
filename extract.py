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
            print("hi")
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

#txt file to analyze
with open('/home/marco/bagfiles/lf2.txt', 'r') as reader:
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

        #extracting time stamp
        if line[4]+line[5]+line[6] == "sec":
            nline = reader.readline()
            time.append(float(line[10:])+float(nline[12:])/1000000000)
        
        
        #next line
        line = reader.readline()

#comment if data should not be filtered
distf = filter(dist)

time = reltime(time)
  
print("\nData extracted")

#plots
xaxis = np.arange(0,len(dist))
plt.scatter(time,dist,color='red',label="not filtered",s=5.0)
#plt.scatter(time,distf,color='green',label="filtered",s=5.0)
plt.legend()
plt.show()
#plt.scatter(xaxis,phi)
#plt.show()
#plt.scatter(xaxis,lane)
#plt.show()






