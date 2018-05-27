#coding=utf-8
#############################################################
#对象的隐藏属性和隐藏方法
#Author:FlashXT;Date:2018.5.19,Saturday;
#CopyRight © 2018-2020,FlashXT & turboMan,All right reserved.
#############################################################
#隐藏属性和方法前加两个下划线,类似与java类中的private变量
class User:

    def __init__(self,user,pwd):

        if len(pwd) >=6:
            #私有属性
            self.__passward = pwd
        else:
            print("密码：%s,不符合规定。"%pwd)
    def __str__(self):
        return self.__passward
    #私有方法
    def __print(self):
        print("AAAAAAAA")

user = User("FlashXT","12324533")

print(user.__str__())