#coding=utf-8
#################################################################################
#类变量和类方法
# Author：FlashXT;
#Date :2018.5.27,Sunday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#################################################################################

class User:
    name = "Tom" #公有类属性
    __age = 20   #私有类属性

    def __init__(self,pwd):
        self.pwd = pwd #对象属性

    @classmethod#类方法在方法上面加上注释
    def print1(cls): #cls表示调用该方法的类
        cls.name = "XiaoMing"
        print("User类方法")
    @staticmethod#静态方法,属于类，没有默认参数(若有参数则必须要传递参数)，可以通通过类名和对象名调用；
    def printA():
        User.name = "AAA"
        print(User.name+" ---> static method")


#类的属性和方法可以通过方法名调用，也可以通过实例名调用；
user = User("123")

print(user.name)
print(User.name)
print(user.print1())
print(user.name)
print(User.name)
print(User.printA())