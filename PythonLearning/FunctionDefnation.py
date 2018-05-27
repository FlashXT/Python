#coding=utf-8
#############################################################
#python 函数定义
#Author:FlashXT;Date:2018.5.19,Saturday;
#CopyRight © 2018-2020,FlashXT & turboMan,All right reserved.
#############################################################

#定义一个函数
def greet_user():              #使用关键字def来告诉Python要定义一个函数。def关键字后面是函数名；
    """显示简单的问候语"""       #此处的文本是被称为文档字符串（docstring）的注释，描述了函数是做什么的。
                               #文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。
    print("Hello!")            #函数体；

greet_user()                      #函数调用；

def greet_user(people = "Tom"):
    """默认问候Tom"""
    print("Welcome,"+people+"!")
greet_user("liBai")




#定义函数并调用
def sum(a,b):
    c = a + b
    print(c)

#调用
sum(9, 90)

#给形参设置默认值，有默认值的形参要定义在无默认值的形参之后
#否则会报错：语法错误：无默认值参数放在了默认值参数之后
#def describe_pet(animal_type="dog", pet_name):
#   """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
# describe_pet(pet_name='harry')  # 关键字参数

#解释：由于给animal_type指定了默认值，无需通过实参来指定动物类型，因此在函数调用中只包含
#一个实参——宠物的名字。然而，Python依然将这个实参视为位置实参，因此如果函数调用中只
#包含宠物的名字，这个实参将关联到函数定义中的第一个形参。这就是需要将pet_name放在形参
#列表开头的原因所在。


def describe_pet(pet_name,animal_type="dog"):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry')  # 调用方法1
describe_pet('DaMao')  # 调用方法2
describe_pet(animal_type="Cat", pet_name='DaGou')

print("=====================")
#不定长参数（列表型）
def PrintNum(a,*args,b=10):
    print("a = "+str(a))
    for i in args:
        print("i = "+str(i))
    print("b = "+str(b))
PrintNum(1,2,3,4,5,6,b=100)

print("=====================")
#不定长参数（字典型）
def PrintNums(a,**args):
    print("a = "+str(a))
    for k,v in args.items():
        print(str(k)+":"+str(v))

PrintNums(1,num1=2,num2=3,num3=4,num4=5)
print("===================")
sum = 0
def Print3(a,*args,**kwargs):
    global sum
    print("a = " + str(a))
    sum+=a
    for i in args:
        print("i = "+str(i))
        sum+=i
    for k,v in kwargs.items():
        print(str(k)+":"+str(v))
        sum+=v

Print3(1,2,3,4,5,6,7,num=10,num2=100)
print("sum = "+ str(sum))