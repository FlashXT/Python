#coding=utf-8
##################################################################
#python class 学习；
# Author：FlashXT;
#Date :2018.5.25,Friday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
##################################################################

class Dog():
	"""一次模拟小狗的简单尝试"""
	def __init__(self,name,age):
		"""初始化属性name 和 age"""
		self.name=name
		self.age=age
	def sit(self):
	    """模拟小狗命令时蹲下"""
	    print(self.name.title()+"is now sitting.")
	def roll_over(self):
	    """模拟小狗命令时打滚"""
	    print(self.name.title()+"roll over!")

dog = Dog("DH",1)
print("My dog's name is "+ dog.name.title()+".")
print("My dog is "+str(dog.age)+" year old.")
print("===============================")
class Restaurant():
	"""定义餐馆类"""
	def __init__(self,name,cuisine_type):
		self.name=name
		self.cuisine_type=cuisine_type
	def describe_restaurant(self):
		print(self.name)
		print(self.cuisine_type)
	def open_restaurant(self):
	    print("open_restaurant")
rest = Restaurant("WuTongYan","Chao")
print(str(rest.name)+str(" "+rest.cuisine_type)+".")
rest.describe_restaurant()
rest.open_restaurant()
print("=====================================")

class servedNums():
	def __init__(self):  # 定义初始化方法
		'''类初始化方法'''
		self.servedNums = 0

	# set方法
	def set_servedNums(self, n):
		'''set方法'''
		self.servedNums = n

	# get方法
	def get_servedNums(self):
		'''get方法'''
		return self.servedNums

	# increment_number_served方法
	def increment_number_served(self):
		self.servedNums += 1

# 实例化类
serNums=servedNums()
print(serNums.get_servedNums())
for i in range(0, 10):
	serNums.increment_number_served()
	print("waiting...")
	i += 1
print(serNums.get_servedNums())
