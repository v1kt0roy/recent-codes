# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:30:16 2021

@author: 0
"""
#对数散点拟合曲线画图
import numpy as np
import matplotlib.pyplot as plt
 # 输入部分
x=[2.3,4.5,3,10000,6.5,40,100]
y=[5,4,7,5,5.3,5.5,6.2]
name=["1","2","3","4","5","6","7"]
fig = plt.figure() 
ax = fig.add_subplot(2,1,1)
ax.set_xscale('log') 
# 拟合对数
result=np.polyfit(np.log(x), y, 1)

q = np.arange(min(x),max(x),(max(x)-min(x))/1000)
 
p =np.log(q)*result[0]+result[1]

plt.plot(q, p)
# 绘图
if len(x)==len(y) and len(x)==len(name):
   for i in range(0,len(x)):
     plt.scatter(x[i],y[i])
     plt.annotate(name[i],(x[i],y[i]))
    
   plt.show()

else:
    raise ValueError("长度不匹配")
