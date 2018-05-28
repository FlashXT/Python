#coding=utf-8
#################################################################################
#NumPy的向量相加
#Author：FlashXT;
#Date :2018.5.27,Sunday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#################################################################################
import numpy
import sys
from datetime import datetime
import sys
#向量相加-python
def pythonsum(n):
	a=[i for i in range(n)]
	b=[i for i in range(n)]
	c=[]
	for i in range(len(a)):
		a[i]=i**2
		b[i]=i**2
		c.append(a[i]+b[i])
	return c

#向量相加-NumPy
def numpysum(n):
	a = numpy.arange(n)**2
	b = numpy.arange(n)**2
	c = a+b
	return c


print("====================")
for i in pythonsum(5):
	print("%-4d"%i,end="")
print("\n====================")
for i in numpysum(5):
	print("%-4d"%i,end="")

#耗时比较
print("\n==============")
size = 1000
start = datetime.now()
c=pythonsum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum",c[-2:])
print("PythonAdd elapsed time in microseconds:",delta.microseconds)

print("\n==============")
size = 1000
start = datetime.now()
c=numpysum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum",c[-2:])
print("PythonAdd elapsed time in microseconds:",delta.microseconds)

#numpy数组
print("===numpy数组======")
a = numpy.arange(5)
print(a.dtype) #数组的数据类型
print(a)       #数组的内容
print(a.shape) #数组的维度信息


#创建多为数组
print("====numpy创建数组1====")
arr = numpy.array([numpy.arange(2),numpy.arange(2)])
print(arr)
print(arr.dtype)
print(arr.shape)

print("====numpy创建数组2:zero()函数====")
print(numpy.zeros(10))
print(numpy.zeros((4,4)))
print(numpy.empty((3,2,2)))
print(numpy.arange(15))
print(numpy.eye(5))

arr=numpy.array([[1,2],[3,4]])

print(arr)
print(arr[1][1])
print(arr.dtype.byteorder)
print(arr.dtype.itemsize)
print("====numpy数据类型====")
print(numpy.int(324))
numstring = numpy.array(["1.25","-9.6","42"],dtype=numpy.string_)
numstring.astype(float)
print(numstring)
#字符编码
print("sys.byteorder = "+sys.byteorder)
print(numpy.arange(7,dtype="f"))
print(numpy.arange(8,dtype="D"))
#dtype类的属性
print("=======dtype类的属性=======")
t = numpy.dtype("Float64")
print(t.char)
print(t.type)
print(t.str)
print("========Python复数========")
a=23+1j
b=1+3j
print(a+b)

print("=======自定义数据类型=======")
t = numpy.dtype([('name',numpy.str_,40),('numtimes',numpy.int32),('price',numpy.float32)])

print(t)
print(t['name'])

#实例化自定义的数据类型
itemz=numpy.array([('Meaning of life DVD',42,3.14),('Butter',13,2.72)],dtype=t)
print(itemz[0])

print("======数组的切片与索引======")
arr = numpy.array(numpy.arange(5))
print(arr)
print(arr.dtype)
print(arr[0:3])
arr2 = numpy.arange(24).reshape(3,2,4)

print(arr2.shape)
print(arr2)

print(arr2[:,0,0])
print(arr2[0])
print(arr2[0,:,:])
print(arr2[0,...])
print(arr2[0,1])
print(arr2[0,1,0:3])
print(arr2[0,1,::2])
print(arr2[...,1])
print(arr2[:,1])
print(arr2[0,:,-1])
#反转矩阵
print(arr2[::-1])
print(arr2[0,::-1,1])
#利用切片函数
s=slice(None,None,1)
print(arr2[...,s])

#布尔型索引
print("=======布尔型索引=======")
names = numpy.array(["Bob","Joe","Will","Tom","Flash","Kim"])
data = numpy.random.randint(10,size=(3,4))#3行4列
data2 = numpy.random.randn(3,4)
data3 = numpy.random.random((3,4))
print(names)
print(data)
print(data2)
print(data3)

names == "Tom"
data4=[names=="Tom"]
print(data4)
data5=[(names=="Tom")[2:]]
print(data5)
data6=[(names=="Tom")[3]]
print(data6)