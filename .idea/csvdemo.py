#encoding: utf-8
import csv
import numpy as np
import matplotlib.pyplot as plt
with open(r"C:\Users\z\Desktop\Daily+News+for+Stock+Market+Prediction\DJIA_table.csv") as c:
    r = csv.reader(c)

    Date,Open,High,Low,Close,Volume,Adj_Close = [],[],[],[],[],[],[]
    index = 0
    for i in  r :
        if(index !=  0 ):
            Date.append(i[0])
            Open.append(i[1])
            High.append(i[2])
            Low.append(i[3])
            Close.append(i[4])
            Volume.append(i[5])
            Adj_Close.append(i[6])
        #print(i)
        index =index+1
    list = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj_Close']
    list1 = ['o', '*', 'v', '-.', '--', 'x']
    lists = {};
    #lists["Date"],lists["Open"],lists["High"],lists["Low"],lists["Close"],lists["Volume"],lists["Adj_Close"] = Date,Open,High,Low,Close,Volume,Adj_Close
    lists["Open"],lists["High"],lists["Low"],lists["Close"],lists["Volume"],lists["Adj_Close"] = Open,High,Low,Close,Volume,Adj_Close
#print(lists)
"""  制图开始   """
list = [ 'Open', 'High', 'Low', 'Close','Volume', 'Adj_Close']
list1 = ['-', '_', 'v', '-.', ':', ':']
colors = ['r','y','g','b','m','k']
"""开始画图"""
fit =plt.figure()
#组装 legends 对象
legends = {}
for i in range(len(list)):
    legends[list[i]]= list1[i]
print(legends)

x = [x for x in range(len(lists["Open"]))]
for index,t in  enumerate(legends.keys()):#迭代
    #print(index,t,list[index])
    fit.add_subplot("61%s"%(index + 1 ))#subplot 页面布局
    plt.plot(x,lists[list[index]],legends[t],color = colors[index])#填充数据（1.x轴数据，2,.y轴数据，3.线条，4.颜色）
    plt.legend(t,loc ="upper left" )
plt.show()