#coding=utf-8
#################################################################
#NumPy中reshape和resized的区别
#Author：FlashXT;
#Date :2018.6.4,Monday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#################################################################
import numpy as np
#例子：模仿随机漫步
import random as rd
position = 0
walk = [position]
steps = 100
for i in xrange(steps):
	step = 1 if rd.randint(0,1) else -1
	position +=step
	walk.append(position)
#print(walk)
walk2=[]
np.random.seed(12345)
nsteps = 10
draws = np.random.randint(0,2,size=nsteps)
steps = np.where(draws > 0,1,-1)
print(steps)
walk2 = steps.cumsum()
print(walk2)
print(walk2.min())
print(walk2.max())
print("=================模拟多个随机漫步===================")
nwalks = 5
nsteps = 3
#draws 每行存储一个代表随机漫步的概率数组
draws = np.random.randint(0,2,size=(nwalks,nsteps)) #0 or 1
print(draws)
#steps 根据draws的内容产生每一个随机漫步的内容
steps = np.where(draws > 0,1,-1)
print(steps)
#对steps矩阵的每行求和，计算每一个随机漫步的结果
walks = steps.cumsum(axis = 1)
print(walks)
print(walks.max())
print(walks.min())

hits2 = (np.abs(walks) >= 2).any(1)#每行中 是否存在>=2的值
print(hits2)
print(hits2.sum()) #统计walks中存在值>=2的随机漫步的数量
crossing_times = (np.abs(walks[hits2])>= 2).argmax(1)
print(crossing_times)

print(crossing_times.mean())