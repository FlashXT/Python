#coding=utf-8
#####################################################################
#keywords
# Author：FlashXT;
#Date :2018.5.25,Friday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#####################################################################
import keyword

print(keyword.kwlist)

a=35
b=5
print("a=%d"%a)
print("a+b=%d"%(a+b))
#python%表示转义
print("输出百分数：%d%%"%a)

#python2中input函数输入的内容作为表达式；
#python3中input函数输入的内容作为字符串；python2中对应raw_input;
a=input("请输入任意值：")
print(a)

name="XiaoHua"
age=23
print("Name:%s,Age:%d"%(name,age+2))

def changeA():
    global a
    a=100
    print(a)

changeA()