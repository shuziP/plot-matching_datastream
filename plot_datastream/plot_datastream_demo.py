import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math



##########
ED = pd.read_csv("ElectricDevices_TEST",header=None)

i=0
x2=list()
y2=list()
# print(len(y1))
# while i <len(y1):
#
#     x.append(i);
#     y.append(y1[i]);
#     i=i+1
def find_max(x1,x2,x3,x4,x5,x6):
    max = x1





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



ave6 = np.delete(ave6, 0, axis=0)
ave5 = np.delete(ave5, 0, axis=0)
ave4 = np.delete(ave4, 0, axis=0)
ave3 = np.delete(ave3, 0, axis=0)
ave2 = np.delete(ave2, 0, axis=0)
ave1 = np.delete(ave1, 0, axis=0)


ave6 = ave6/len(list_6)
ave5 = ave5/len(list_5)
ave4 = ave4/len(list_4)
ave3 = ave3/len(list_3)
ave2 = ave2/len(list_2)
ave1 = ave1/len(list_1)
print(ave6)

######################################################################
data = pd.read_csv('DataStream',header=None)
y1 = np.array(data)

plt.ion() ## Note this correction
fig=plt.figure()
#plt.axis([0,1000,0,1])

i=1
x=list()
y=list()
A_list=[]

def distance(y1,y2):
    for j in range(1,7):
        print(j)




while i <len(y1):

    temp_y=np.random.random();
    plt.axis([0,97,-2,10 ])
    if i > 95:
        #x.append(x[i-97])
        del y[0]
    else:
        x.append(i);
    y.append(y1[i]);
    yy1 = np.array(y)#当前列表的数字

    #ave各个标签的数组

    #print(len(ave1),len(yy1))
    ay1 = abs(yy1 - ave1)*abs(yy1 + ave1)
    ay2 = abs(yy1 - ave2)*abs(yy1 + ave2)
    ay3 = abs(yy1 - ave3)*abs(yy1 + ave3)
    ay4 = abs(yy1 - ave4)*abs(yy1 + ave4)
    ay5 = abs(yy1 - ave5)*abs(yy1 + ave5)
    ay6 = abs(yy1 - ave6)*abs(yy1 + ave6)
    A_list =[ay1.sum(),ay2.sum(),ay3.sum(),
             ay4.sum(),ay5.sum(),ay6.sum()]
    # while i >95:
    #
    #     print("\nyy1:",yy1,"\nave1:",ave1,"\nay1:",ay1,"\nsum:",ay1.sum())
    #     break


    #if i %96 ==0:





    #
    # if x1[0]>2:
    #     plt.plot(x, y, 'r*-');

    if i%96==0:
        #print(i)
        if min(A_list) ==A_list[0]:
            o=1
        if min(A_list) ==A_list[1]:
            o=2
        if min(A_list) ==A_list[2]:
            o=3
        if min(A_list) ==A_list[3]:
            o=4
        if min(A_list) ==A_list[4]:
            o=5
        if min(A_list) ==A_list[5]:
            o=6



        print("读入第",i,"个数据", A_list, "    差距最小距离位：", math.sqrt(min(A_list)),"\n","当前波段最符合类型：",o,"\n")
        plt.plot(x, y, 'r*');
    elif (i-1)%96==0:
        plt.plot(x, y, 'r--');
    elif (i-2)%96==0:
        plt.plot(x, y, 'r--');
    elif (i-3)%96==0:
        plt.plot(x, y, 'r*-');
    elif (i-4)%96==0:
        plt.plot(x, y, 'r--');
    elif (i-5)%96==0:
        plt.plot(x, y, 'r--');


    else:
        plt.plot(x,y,'k-');
    i+=1;
    plt.show()

    plt.pause(0.00001) #Note this correction
    plt.cla()


    ################
    # while i < 1000:
    #
    #     temp_y = np.random.random();
    #     if i > 97:
    #         x.append(x[i - 97])
    #     else:
    #         x.append(i);
    #     y.append(y1[i]);
    #
    #     plt.plot(x, y, 'r-');
    #     i += 1;
    #     plt.show()
    #     plt.pause(0.0001)  # Note this correction