#coding=utf-8
#####################################################################
#class extends
# Author：FlashXT;
#Date :2018.5.25,Friday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#python继承的实现：
#    super()是一个特殊函数，帮助Python将父类和子类关联起来。这行代码让Python
# 调用父类的方法__init__()，让子类实例包含父类的所有属性。父类也称为超类
# （superclass），名称super因此而得名。
#     函数super()需要两个实参：子类名和对象self。为帮助Python将父类和子类关联
# 起来，这些实参必不可少。另外，在Python 2.7中使用继承时，务必在定义父类时在括号
# 内指定object。
#####################################################################

#定义父类
class Person(object):
	def __init__(self,name,sex,age,stature):
		self.name = name
		self.sex  = sex
		self.age = age
		self.stature = stature
	def Eat(self,time,food):
		print(self.name+" eat "+food+" at "+time+".")
	def Walk(self,longth):
		print(self.name+" walk about "+longth+"km.")
	def dress(self,color):
		print(self.name+" dress a clothes in "+color+" color.")
	def live(self,floor):
		print(self.name+" live in "+floor+" floor.")
	def getInfo(self):
		print("====================")
		print("Name:\t"+self.name)
		print("Sex:\t"+self.sex)
		print("Age:\t"+self.age)
		print("Stature:"+self.stature)
class Student(Person):
	def __init__(self,name,sex,age,stature,major):
		super().__init__(name,sex,age,stature)
		self.major=major
	def learn(self,course):
		print(self.name+" is learning "+course+" !")
	def getInfo(self):
		super().getInfo()
		print("Major:\t"+self.major)
class Teacher(Person):
	def __init__(self,name,sex,age,stature,teach):
		super().__init__(name,sex,age,stature)
		self.teach=teach
	def teaching(self,course):
		print(self.name+" is teaching "+course+" !")
	def getInfo(self):
		super().getInfo()
		print("Teach:\t"+self.teach)
#实例化Person
person=Person("turboMan","Female","23","162")
person.getInfo()
#实例化
stu=Student("FlashXT","Male","25","170","Math")
stu.getInfo()
#实例化teacher
teach=Teacher("XiaomMing","Female","30","163","English")
teach.getInfo()
print("==================Eat======================")
person.Eat("afternoon","noodles")
stu.Eat("afternoon","noodles")
print("===================Walk====================")
person.Walk("10")
stu.Walk("10")
print("==================dress====================")
person.dress("Red")
stu.dress("Black")
print("=================live======================")
person.live("11")
stu.live("11")
print("================Skill======================")
stu.learn("Programing")
teach.teaching("English")
print("==========isinstance==========")
print("stu is a instance of Student. ") if isinstance(stu,Student) else 0
print("stu is a instance of Person.")if isinstance(stu,Person) else 0

#多态(严格上将不算多态)
def Palying(Student,game):
	print(Student.name+" is playing 》"+game.upper()+" !")
print("============Palying===============")
Palying(person,"Tomb Radier")
Palying(stu,"Cross Fire")
Palying(teach,"CsGO")