#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

dist = []
phi = []
lane = []

with open('/home/marco/bagfiles/movement.txt', 'r') as reader:
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
        '''
        #extracting in_lane
        if line[0]+line[1] == "in":
            if line[9]=="T":
                lane.append(1)
                #print(line[9])
            else:
                lane.append(0)
                #print(line[9])
        '''
        
        #next line
        line = reader.readline()
  
print("\nData extracted")

#plots
xaxis = np.arange(0,len(dist))
plt.scatter(xaxis,dist)
plt.show()
plt.scatter(xaxis,phi)
plt.show()
#plt.scatter(xaxis,lane)
#plt.show()



