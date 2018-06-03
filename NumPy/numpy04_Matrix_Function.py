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