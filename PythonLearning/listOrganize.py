#coding=utf-8
##################################################################
#练习python 中list的组织；
# Author：FlashXT;
#Date :2018.5.17,Thursday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
##################################################################
list = [1,13,4,23,56,3,67,89,21]
print(sorted(list))
print(list)
list.reverse()
print(list)
print (len(list))
#list遍历
for i in range(len(list)):
	print (list[i])
#foreach
for i in list:
    print (i)
print ("===================================")
a  = range(1,11)
print (a)
print (type(a))
print ("===================================")
b= [i for i in range(1,11)]
print (b)
print (type(b))
print (min(b))
print (max(b))
print (sum(b))

#列表解析（表达式）
list = [value**2 for value in range(1,11)]
print (list)