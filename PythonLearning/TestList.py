#coding=utf-8
##################################################################
#练习使用 python 中list的各种方法；
# Author：FlashXT;
#Date :2018.5.17,Thursday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
##################################################################
list = ['a','b','c','d']
#[0,1)访问区间为前闭后开
print(list[0:1])
print(list[0:3])
#下面3种访问方法等价
print (list[0:4])
print(list[0:6])
print(list[0:])
#最后一个元素下标为-1
print(list[-3:-1])
print (list[-3:])
#设置凡访问步长，list[始下标：终下标：步长]
print (list[0:4:2])

#修改list中的元素
list[3]=123
print(list)
#在list的末尾添加元素
list.append("AAAA")
#在指定位置添加元素
list.insert(3,"BBBB")
print (list)
#删除list末尾的元素并返回
k = list.pop()
print (list,k)
#删除指定位置的元素
m = list.pop(3)
print (list,m)
del list[2]
print (list)

#根据值删除元素,元素比存在会报错
list.remove('a')
print(list)