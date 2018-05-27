#coding=utf-8
#################################################################################
#多态
# Author：FlashXT;
#Date :2018.5.27,Sunday;
#Copyright © 2018–2020 FlashXT and turboMan. All rights reserved.
#################################################################################

class A:
    def test(self):
        print("A -----> text()")
class B(A):
    def test(self):
        print("B -----> text()")
class C(B):
    def test(self):
        print("C -----> text()")

def Test2(obj):
    print(obj.test())

c = C()
Test2(c)