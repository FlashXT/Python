#coding=utf-8
#################################################################
#NumPy Matrix Function
#Author：FlashXT;
#Date :2018.6.1,Friday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#################################################################
import numpy as np
x= np.random.randint(1,9,(3,3))
print("x = \n"+str(x))
print("==============")
y=np.random.randint(1,10,(3,4))
print("y = \n"+str(y))
print("==============")
print("x*y = \n"+str(x.dot(y)))
print("==============")
print("x*y = \n"+str(np.dot(x,y)))
print("==============")
print("=========矩阵的迹trace:对角线元素的和=========")
print("X(trace) = " + str(np.trace(x)))
arr=np.eye(4)
print("arr = \n"+str(arr))

print("arr(det) = "+ str(np.linalg.det(arr)))
print("x.eig特征值 = \n"+str(np.linalg.eig(x)))
arr2=np.random.randint(1,10,(3,3))
print("arr2 = \n "+ str(arr2))
print("arr2的逆 = \n"+ str(np.linalg.inv(arr2)))
print("arr2的Moore-Penrose伪逆 = \n"+ str(np.linalg.pinv(arr2)))
arr3 = np.mat("3 2 1;4 4 7;7 8 9")
print("arr3 = \n"+str(arr3))
print("arr3的QR分解 = \n " + str(np.linalg.qr(arr3)))
print("arr3的奇异值分解(SVD) = \n"+str(np.linalg.svd(arr3)))
print("==================线性方程组求解====================")
#solve函数有两个参数a和b。a是一个N*N的二维数组，而b是一个长度为N的
# 一维数组，solve函数找到一个长度为N的一维数组x，使得a和x的矩阵乘积
# 正好等于b，数组x就是多元一次方程组的解。
a=np.mat("1 2 3 4;3 5 6 7;4 3 2 2;1 3 5 0")
b=[0,1,1,2]
print(np.linalg.solve(a,b))
#AX=B的最小二乘解
print(np.linalg.lstsq(a,b,None))

print("===============随机数生成==============")
from random import normalvariate
samples = np.random.normal(size=(4,4))
print(samples)
N=1
#see()方法用于设置产生随机数的种子，之后需要调用random()方法产生随机数
#seed( ) 用于指定随机数生成时所用算法开始的整数值。
#1.如果使用相同的seed( )值，则每次生成的随即数都相同；
#2.如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。
#3.设置的seed()值仅一次有效
np.random.seed(N)
i=0
while( i in range(7)):
	print(np.random.random())
	i+=1
arr=[1,2,3,4,5,6,7,8,9]
#permutation()返回一个序列的随机排列或返回一个随机排列的范围
print(np.random.permutation(arr))
#shuffle()对一个序列就地随机排列
np.random.shuffle(arr)
print(arr)
#rand()产生均匀分布的样本值
arr2=np.random.rand(5,3)
print(arr2)
#binomial()产生二项分布的样本值
arr3=np.random.binomial(3,0.5,(3,4))
print(arr3)
#normal(loc=0.0,scale=1.0,size=None)产生正态(高斯)分布的样本值
#参数的含义：
# ①loc:float    此概率分布的均值；
# ②scale：float 此概率分布的标准差；
# ③size:int or tuple of ints 输出的矩阵维度，默认为None,只输出一个值

arr4=np.random.normal(0,1,(3,4))
print(arr4)

#beta(a,b,size)产生beta分布的样本值
arr5=np.random.beta(1,2,(3,4))
print(arr5)
print("==================矩阵求和==================")
arr6=np.array([1,2,3,4,5,6,7,8]).reshape(2,4)
print(arr6)
print(arr6.cumsum())
print(arr6.cumsum(axis=1))
print("==========================")
print(arr6.cumprod())
