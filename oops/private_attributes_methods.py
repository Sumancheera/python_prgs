# private(like) attributes and methods 
# are meant to be used only within cls & not accessable from outside the cls.
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #making attribute private by adding __brfore attribute
    def resetpass(self):
        print(self.__acc_pass)

    

acc1=Account(280601501074,"suman100")
print(acc1.acc_no)
##print(acc1.__acc_pass)
print(acc1.resetpass())

# private methods or functions
class Person:
    __name="anonymous"

    def __hello(self):
        print("hello person")
    def hello(self):  # or welcome(self): to print pvt her then call public welcome() to acces __hell() out side fun
        self.__hello()

p1=Person()
p1.hello() #accessing pvt method, outside cls
