#coding=utf-8
##################################################################
#字典练习；
# Author：FlashXT;
#Date :2018.5.17,Thursday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
##################################################################

dic= {"Name":"Flash","Sex":"Male","Age":"21"};
for key in dic.keys():
	print (key)
print("========================")
for value in dic.values():
	print (value)
print("========================")
for key,value in dic.items():
	print (key+":"+value)
#列表嵌套字典
xiaoMing={"Name":"XM","Sex":"Male","Age":"21"}
xiaoHong={"Name":"XH","Sex":"FeMale","Age":"20"}
xiaoLi={"Name":"XL","Sex":"Male","Age":"24"}
Students = [xiaoMing,xiaoHong,xiaoLi]
for i in Students:
	print (i)
#字典嵌套列表
Stus = {"XM":["A","B"],"XH":["C","D"],"XL":["E","F"]}
for key,value in Stus.items():
	print(key)
	for i in value:
		print (i)
	print("==============")
#字典嵌套字典
Stu={"XM":xiaoMing,"XH":xiaoHong,"XL":xiaoLi}
for key,value in Stu.items():
	print(key)
	for i in value.items():
		print (i)
	print("==============")