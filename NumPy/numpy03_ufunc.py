#coding=utf-8
#################################################################
#NumPy 通用函数 ufanc
#Author：FlashXT;
#Date :2018.5.29,Tuesday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#################################################################
from __future__ import division
from numpy.random import randn
import numpy as np
import matplotlib.pyplot as plt
#通用函数
arr = np.arange(9).reshape(3,3)
print(arr)
print(np.sqrt(arr[1][1]))
print("%7.4f"%np.exp(arr[1][1]))#exp函数计算e^x的值，x为传递的参数

x=randn(8)
y=randn(8)
print(x)
print(y)
print(np.maximum(x,y))#元素级最大值

arr2=randn(7)
arr3=randn(7)*5
print("arr2 = "+str(arr2))
print("arr3 = "+str(arr3))
print("arr4 = "+str(arr2*5))
print("==========利用数组进行数处理==========")
#向量化
points = np.arange(-5,5,0.01)#1000 equally spaced points
xs,ys=np.meshgrid(points,points)
print(xs)

z=np.sqrt(xs**2+ys**2)
plt.imshow(z,cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid of values")
plt.draw()
#plt.show()
#将条件逻辑表达为数组运算
print("==========将条件逻辑表达为数组运算============")
xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True,False,True,True,False])

result = [x if c else y for x,y,c in zip(xarr,yarr,cond)]
print(result)
result2=np.where(cond,xarr,yarr)
print(result2)

arr = randn(4,4)
print(arr)
arr=np.where(arr>0,2,-2)#元素值大于0设为2，否则为-2
print(arr)
arr = np.where(arr>0,1,arr)#元素值大于0设为2，否则为原来的值
print(arr)

result=[]
cond1=[True,False,True,False]
cond2=[False,False,True,True,False]
for i in range(len(cond1)if len(cond1)<len(cond2) else len(cond2)):
	if cond1[i] and cond2[i]:
		result.append(0)
	elif cond1[i]:
		result.append(1)
	elif cond2[i]:
		result.append(2)
	else:
		result.append(3)
print(result)
result2=[]
for i in range(len(cond1)if len(cond1)<len(cond2) else len(cond2)):
	result2.append(np.where(cond1[i]&cond2[i],0,
	                 np.where(cond1[i],1,
	                          np.where(cond2[i],2,3))))
print(result2)
print("=========数学与统计学方法==========")
arr4 = np.random.randn(3,3)#标准正态分布数据
print(arr4)
#下面两种方法等效
print(arr4.mean())
print(np.mean(arr4))
print(np.mean(arr4,axis=0)) #axis=0,计算每一列的均值
print(np.mean(arr4,axis=1)) #axis=0,计算每一行的均值
print("arr4 = "+str(arr4.sum(0)))#第一列的和