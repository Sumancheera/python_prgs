#Encapsulation: Encapsulation is the bundling of data (attributes) and methods (functions) within a class, 
#restricting access to some components to control interactions.

# private(like) attributes and methods 
# are meant to be used only within cls & not accessable from outside the cls.
class Account:
    def __init__(self,acc_no,acc_pass,pass_hint):
        self.acc_no=acc_no # Public attribute
        self.__acc_pass=acc_pass #making attribute private by adding __brfore attribute. # Private attribute
        self._pass_hint=pass_hint # Protected attribute
    def resetpass(self):
        print(self.__acc_pass)

acc1=Account(280601501074,"suman100","name related")
print(acc1.acc_no)
##print(acc1.__acc_pass)
print(acc1.resetpass())
print(acc1._Account__acc_pass,"printing the renamed private member/attibute") #object._classname__privateattributename
print(acc1._pass_hint) #for protected we can still access. but suggested not to use

# private methods or functions
class Person:
    __name="anonymous"

    def __hello(self):
        print("hello person")
    def hello(self):  # or welcome(self): to print pvt her then call public welcome() to acces __hell() out side fun
        self.__hello()
    def printname(self):
        print(Person.__name)

p1=Person()
p1.hello() #accessing pvt method, outside cls
p1.printname()
