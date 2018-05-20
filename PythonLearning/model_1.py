#coding=utf-8
#############################################################
#四则运算模块
#Author:FlashXT;Date:2018.5.19,Saturday;
#CopyRight © 2018-2020,FlashXT & turboMan,All right reserved.
#############################################################

#Add
def add(a=0,b=0):
    """
    :param a:
    :param b:
    :return: a+b
    """
    return a+b
#Sub
def sub(a=0,b=0):
    """
    :param a:
    :param b:
    :return: q-b
    """
    return a-b

#Multi
def Multi(a=1,b=1):
    """
    :param a:
    :param b:
    :return: a*b
    """
    return a*b

#Div
def Div(a=1,b=1):
    """
    :param a:
    :param b:
    :return: a/b
    """
    return (a/b if b!=0 else -1)