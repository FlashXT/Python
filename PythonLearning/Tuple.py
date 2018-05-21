#coding=utf-8
##################################################################
#元组：元组就是不可变列表，元组使用圆括号来标识；
# Author：FlashXT;
#Date :2018.5.17,Thursday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
##################################################################
dims =(1,1,12,13,432,34)
print(dims)
print(dims[0])
dims2 = dims
print (dims2 is dims)

print("=============================")
list01 = [1, 2, 3, 4]
list02 = list01[:]
list03 = list01
print ("list01=" + str(list01))
print ("list02=" + str(list02))

print (list01 == list02 and "list01==list02" or "list01!=list02")
print ("list01==list02")if list01 == list02 else "list01!=list02"

print (list01 is list02 and "list01 is list02" or "list01 isn't list02")
print (list01 is list03 and "list01 is list03" or "list01 isn't list03")