#coding=utf-8
#################################################################
#NumPy中reshape和resized的区别
#Author：FlashXT;
#Date :2018.6.1,Friday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#################################################################
#reshape有返回值，会对原始数据进行修改；
#resizee无返回值，不会对原始数据进行修改；
import numpy as np
x = np.random.rand(2,3)
print("x(原始)=\n"+str(x))
print("====================================")
y=x.reshape((3,2))
print("x(reshape后)=\n"+str(x))
print("====================================")
print("y =x.reshape((3,2))\n"+str(y))
print("====================================")
z=x.resize(3,2)
print("x(resize后)=\n"+str(x))
print("====================================")
print("z =x.resize((3,2))\n"+str(z))
print("====================================")

