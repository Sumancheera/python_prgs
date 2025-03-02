# constructor in inheritance, how it behavies

class A:
    def __init__(self):
        print("in init a")
    
class B(A): #if you have parent init and not child it will call parent init
    def __init__(self): #if has own it will print own
        print("in init b")
        super().__init__() 
    
a1=B()

#MRO(method resolution order, left to right)
print("MRO starts here......................")
class A:
    def __init__(self):
        print("in init a")
    def feature1(self): 
        print("this is feature 1 in A")
class B: #if you have parent init and not child it will call parent init
    def __init__(self): #if has own it will print own
        print("in init b")
    def feature1(self):
        print("this is feature 1 in B")
class C(B,A): #according to MRO it will call which ever is in left
    def __init__(self):
        print("in c init")
        super().__init__()
    def super_method(self):
        super().feature1()
c1=C()
c1.feature1() #if we call method will it folloe mRO.?
c1.super_method()