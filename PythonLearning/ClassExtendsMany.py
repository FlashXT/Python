#coding=utf-8
#################################################################################
#多重继承
# Author：FlashXT;
#Date :2018.5.27,Sunday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#################################################################################

class A:
    def test(self):
        print("A -----> text()")
class B:
    def test(self):
        print("B -----> text()")
class C(A,B):
    def test1(self):
        print("C -----> text()")

c = C()
#为什么调用A.test(),而不是B.text(),这就是多重继承的优先级问题：
# 写在前面的优先级高，也可以调用__mro__()方法查看继承的优先级；
c.test()
print(C.__mro__)