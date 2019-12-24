# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

def ave(x):
    return x

from matplotlib import pyplot as plt
from matplotlib import animation

#data = pd.read_csv('DataStream',header=None)

#data = pd.read_csv('DataStream',header=None)
#y1 = np.array(data)
ED = pd.read_csv("ElectricDevices_TEST",header=None)

i=0
x=list()
y=list()
# print(len(y1))
# while i <len(y1):
#
#     x.append(i);
#     y.append(y1[i]);
#     i=i+1




list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]
list_6=[]

g = ED.T
print(len(ED))


ave6 = np.array(g[0])
ave5 = np.array(g[122])
ave4 = np.array(g[135])
ave3 = np.array(g[739])
ave2 = np.array(g[1062])
ave1 = np.array(g[338])
print(ave6)
for i in range (len(ED)):
    if g[i][0]==6:
        if i != 0:
            ave6 +=np.array(g[i])

        list_6.append(i)
print("list 6:",len(list_6),list_6)

for i in range (len(ED)):
    if g[i][0]==5:
        #print(i)
        if i != 122:
            ave5 += np.array(g[i])
        list_5.append(i)
print("list 5:",len(list_5),list_5)

for i in range (len(ED)):
    if g[i][0]==4:
        if i!= 135:

            ave4 += np.array(g[i])
        #print(i)
        list_4.append(i)
print("list 4:",len(list_4),list_4)

for i in range (len(ED)):
    if g[i][0]==3:
        if i != 793:
            ave3 += np.array(g[i])
        #print(i)
        list_3.append(i)
print("list 3:",len(list_3),list_3)

for i in range (len(ED)):
    if g[i][0]==2:
        if i != 1062:
            ave2 += np.array(g[i])
        #print(i)
        list_2.append(i)
print("list 2:",len(list_2),list_2)

for i in range (len(ED)):
    if g[i][0]==1:
        if i != 338:
            ave1 += np.array(g[i])
        #print(i)
        list_1.append(i)
print("list 1:",len(list_1),list_1,)


ave6 = ave6/len(list_6)
ave5 = ave5/len(list_5)
ave4 = ave4/len(list_4)
ave3 = ave3/len(list_3)
ave2 = ave2/len(list_2)
ave1 = ave1/len(list_1)
print(ave6)

