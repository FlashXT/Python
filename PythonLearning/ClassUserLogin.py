#coding=utf-8
##################################################################
#python class 学习；
# Author：FlashXT;
#Date :2018.5.25,Friday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
##################################################################
print("===========UserLogin===========")
class userlogin():
	def __init__(self):
		"""类初始化方法"""
		self.loginattempts=0
	def get_loginattempts(self):
		return self.loginattempts
	def set_loginattempts(self,times):
		self.loginattempts=times
	def increment_login_attempts(self):
		self.loginattempts+=1
#实例化类
ul=userlogin()

print(ul.get_loginattempts())

for i in range(0,100):
	ul.increment_login_attempts()
	i+=1
print(ul.get_loginattempts())