#coding=utf-8
#################################################################################
#__init__方法和__del__方法：
#__init__方法在创建类的实例时由系统自动调用，创建类的实例；
#__del__方法在销毁类的实例时由系统自动调用，销毁对象(当且仅当该实例没有任何引用指向);整个
# 程序运行结束时，也会调用__del__方法销毁所有内存中的对象；
#Author：FlashXT;
#Date :2018.5.27,Sunday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#################################################################################

class User():
    def __init__(self,name):
        self.name = name
        print(self.name)
    def __del__(self):
        print("销毁实例!")
print("*_*"*30)
user1 = User("AAA")
user2 = user1
print("'='"*30)
del user1
print("~~~"*30)
print(user2.name)