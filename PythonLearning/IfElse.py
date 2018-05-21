#coding=utf-8
##################################################################
#IfElse
# Author：FlashXT;
#Date :2018.5.17,Thursday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
##################################################################
nums=int(input("请输入整数：")) #读取用户输入
if nums<10:
    print ("nums<10")
elif nums<=20:
	print ("nums<=20")
else :
	print ("nums>20")

print (1 and 2 or 3)
print (1 or 2 and 3)
print (1 is 3)
print (not 0)