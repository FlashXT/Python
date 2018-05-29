#coding=utf-8
#################################################################
#NumPy学习
#Author：FlashXT;
#Date :2018.5.29,Tuesday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#################################################################
import numpy as np
print("=======组合数组=======")
a=np.arange(9).reshape(3,3)
print(a)
b = 2*a
print(b)
print np.hstack((a,b))#水平组合
print np.concatenate((a,b),axis=1)#水平组合

print np.vstack((a,b))#垂直组合
print np.concatenate((a,b),axis=0)#垂直组合
print np.dstack((a,b))
oned = np.arange(2)
toned = 2*oned
print oned,toned
print np.column_stack((oned,toned))#一维数组列组合
print np.column_stack((a,b)) #二维数组列组合（与水平组合相同）
print np.row_stack((oned,toned))#一维数组行组合
print np.row_stack((a,b))#二维数组行组合（与垂直组合相同）
#数组的分割
print("=========数组的分割=========")
s=np.arange(9).reshape(3,3)
print(a)
print(np.hsplit(a,3))#垂直分割
print(np.split(a,3,axis=1))#垂直分割
print(np.vsplit(a,3))#水平分割
print(np.split(a,3,axis=0))#水平分割
c = np.arange(27).reshape(3,3,3)
print(c)
print(np.dsplit(c,3))#深度分割
print("==========数组的属性==========")
print(c.ndim)
print(c.size)
print(c.itemsize)
print(c.nbytes)
d=np.array([1+1j,3+2j])
print(d)
print(d.real)
print(d.imag)
e = np.arange(4).reshape(2,2)
f = e.flat#将e按行拉伸为一维数组
print(e)
print(f)
print(e.flat[1],e.flat[2])#输出拉伸后的一维数组中的第3个元素
print("==================数组的转换==================")
g = np.arange(9).reshape(3,3)
print(g)
print(g.tolist())
print(g.tostring())
print(np.fromstring("\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?"))
print(np.fromstring("20:42:52",sep=":",dtype=int))
print("=====================")
h=np.array([1+1j,3+2j])
i=h.astype(int)#只保留实部，有数据丢失
print(i)
print(i.astype("complex"))