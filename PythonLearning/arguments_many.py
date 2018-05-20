#coding=utf-8
#############################################################
#函数接收任意个参数
#Author:FlashXT;Date:2018.5.20,Sunday;
#CopyRight © 2018-2020,FlashXT & turboMan,All right reserved.
#############################################################

#接收任意个参数
# 形参名前加上*号，表示让Python创建一个空元组，并将收到的所有值都封装到这个元组中；
def make_pizza(*toppings):
    """Make Pizza"""
    for topping in toppings:
        print("Adding "+topping +"...")
    print("Finished!")
make_pizza("12321")
make_pizza("A","B","C","D","E","F")

#结合使用位置实参和任意数量实参
#如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
#Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
def make_pizza(size,*toppings):
    """Make Pizza by any size"""
    print("Make a pizza of "+size+" inch..." )
    for topping in toppings:
        print("Adding " + topping + "...")
    print("Finished!")
make_pizza("12","A","B","C","D","E")

#使用任意数量的关键字实参
#有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，
#可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
# 使用任意数量的关键字实参
def userinfos(first, last, **userinfo):
    """创建一个字典，其中包含用户信息"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in userinfo.items():
        profile[key] = value
    return profile


userinfo = userinfos("First", "Last", location="China", City="Xi'an")
print("===================")
for key, value in userinfo.items():
    print(str(key) + " : " + str(value) + ";")

# 函数build_profile()的定义要求提供名和姓，同时允许用户根据需要提供任意数量的名称—值
# 对。形参 ** user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所
# 有名称—值对都封装到这个字典中。在这个函数中，可以像访问其他字典那样访问user_info中的
# 名称—值对。

