import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from time import sleep
import itertools #用于拆分list的模块 a = list(itertools.chain.from_iterable(a))


##########
#C:\Users\shuzip\Desktop\project1 2\project1\data
ED = pd.read_csv(r"data/ElectricDevices_TEST",header=None)

i=0
x2=list()
y2=list()



g = ED.T      #ElectricDevices转置为列向量
h=g.drop([0]) #获得删去标签后的 ElectricDevices
list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]
list_6=[]


print(len(ED))


ave6 = np.array(g[0])
ave5 = np.array(g[122])
ave4 = np.array(g[135])
ave3 = np.array(g[739])
ave2 = np.array(g[1062])
ave1 = np.array(g[338])
print(ave6)

ED2 = np.array(ED.T)

ED2 = np.delete(ED2, 0, axis=0)
ED2 = ED2.T
print("ED2:\n",len(ED2[1]),"\nED2\n")



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


#删除头列的标记
ave6 = np.delete(ave6, 0, axis=0)
ave5 = np.delete(ave5, 0, axis=0)
ave4 = np.delete(ave4, 0, axis=0)
ave3 = np.delete(ave3, 0, axis=0)
ave2 = np.delete(ave2, 0, axis=0)
ave1 = np.delete(ave1, 0, axis=0)

#求各列平均值
ave6 = ave6/len(list_6)
ave5 = ave5/len(list_5)
ave4 = ave4/len(list_4)
ave3 = ave3/len(list_3)
ave2 = ave2/len(list_2)
ave1 = ave1/len(list_1)
print(ave6)

######################################################################
#读入数据流
data = pd.read_csv(r'data/DataStream',header=None)
y1 = np.array(data)

plt.ion() ## Note this correction
fig=plt.figure()
#plt.axis([0,1000,0,1])

#datastream实现
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3,rowspan=2)

#ax1.plot([1, 2], [1, 2])    # 画小图
ax1.set_title('datastream')  # 设置小图的标题




#ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)

ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))
ax6 = plt.subplot2grid((3, 3), (2, 2), rowspan=1)
#ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('most similar image')
ax4.set_ylabel(' ')
ax5.set_xlabel(' ')
ax6.set_xlabel(' ')

ax4.axis([0,97,-2,10 ])
ax5.axis([0,97,-2,10 ])
ax6.axis([0,97,-2,10 ])



D = 0
i=1
k = 0
kk = k
x=list() #x轴数据
y=list() #y轴数据
A_list=[] #存储各个标签的差值
com_1 = x
com_min =10000

while i <=len(y1):

    temp_y=np.random.random();
    ax1.axis([0,97,-2,10 ])
    if i > 96:
        #x.append(x[i-97])
        del y[0]
    else:
        x.append(i);
    y.append(y1[i]);
    yy1 = np.array(y)#当前列表的数字

    if i >96:
        #com_min = 100
        if i % 96 == 0:
            com_min = 100
        while k < 7711:
            yy2 = np.array(list(itertools.chain.from_iterable(y)))
            com_1 = yy2 - ED2[k]
            com_1 = com_1 *com_1

            # num = float(xx.T * ED2[k])  # 若为行向量则 A * B.T
            # denom = linalg.norm(xx) * linalg.norm(ED2[k])
            # cos = num / denom  # 余弦值
            if com_1.sum() <10 :

                if k in list_1:
                    D  = 1

                if k in list_2:
                    D  = 2
                if k in list_3:
                    D  = 3
                if k in list_4:
                    D  = 4
                if k in list_5:
                    D  = 5
                if k in list_6:
                    D  = 6
                ax5.cla()
                ax5.plot(ED2[k],"r")
                s5 = 'best match :'+ str(k) +"\nThe label is "+ str(D)
                ax5.set_xlabel(s5)


            if com_1.sum() <30:
                ax6.cla()
                ax6.plot(ED2[k],'g')

                print("读入",i ,"个数据：","与第",k,"个数据组的比对结果为：","||",com_1.sum())
                if com_min >com_1.sum():
                    com_min = com_1.sum()
                    ax4.cla()
                    ax4.plot(ED2[k])
                    s = 'most similar image'
                    ax4.set_xlabel(s)

                #ax4.plot(ED2[k])



                # if kk -k <-50:
                #     kk =k
                # #plt.pause(0.000001)
                # #sleep(0.1)
                #
                #     ax4.cla()
                #     ax4.plot(ED2[kk])

                #print(yy2.T,"\n",ED2[k].T)
            k = k+1
        k = 0




    #ave各个标签的数组

    #print(len(ave1),len(yy1))
    #各个表情与当前数据的相减
    # ay1 = abs(yy1 - ave1)
    # ay2 = abs(yy1 - ave2)
    # ay3 = abs(yy1 - ave3)
    # ay4 = abs(yy1 - ave4)
    # ay5 = abs(yy1 - ave5)
    # ay6 = abs(yy1 - ave6)
    #
    #
    # ay1 = ay1*ay1
    # ay2 = ay2*ay2
    # ay3 = ay3*ay3
    # ay4 = ay4*ay4
    # ay5 = ay5*ay5
    # ay6 = ay6*ay6
    #
    #
    # A_list =[ay1.sum(),ay2.sum(),ay3.sum(),
    #          ay4.sum(),ay5.sum(),ay6.sum()]






    #
    # if x1[0]>2:
    #     plt.plot(x, y, 'r*-');

    if i%96==0:
        print(i)
        # if min(A_list) ==A_list[0]:
        #     o=1
        # if min(A_list) ==A_list[1]:
        #     o=2
        # if min(A_list) ==A_list[2]:
        #     o=3
        # if min(A_list) ==A_list[3]:
        #     o=4
        # if min(A_list) ==A_list[4]:
        #     o=5
        # if min(A_list) ==A_list[5]:
        #     o=6


    #
    #     print("读入第",i,"个数据", A_list, "    差距最小距离位：", math.sqrt(min(A_list)),"\n","当前波段最符合类型：",o,"\n")
    #     #闪烁效果实现
        #ax1.plot(x, y, 'r*');
    elif (i-1)%96==0:
        ax1.plot(x, y, 'r--');
    elif (i-2)%96==0:
        ax1.plot(x, y, 'r--');
    # elif (i-3)%96==0:
    #     ax1.plot(x, y, 'r*-');
    elif (i-4)%96==0:
        ax1.plot(x, y, 'r--');
    elif (i-5)%96==0:
        ax1.plot(x, y, 'r--');


    else:
        ax1.plot(x,y,'k-');
    i+=1;




    #ax5.plot(h[0])
    #ax5.plot(g[0].drop([0]))








    plt.show()

    plt.pause(0.00001) #Note this correction
    ax1.cla()   #擦除已经生成的图像


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