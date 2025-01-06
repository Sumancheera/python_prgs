# getting attributes or methods from parent class
# inheritence,multi-level inhe, multiple inheritence

#single inheritence:
class Car:
    colour="balck"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car): #inheritence used
    def __init__ (self,name):
        self.name=name

car1= Toyotacar("fortuner")
car2= Toyotacar("innova")
print(car1.name)
car1.start() #inheritence used
print(car1.colour)
car2.stop()

# multi-level inheritence:
class Car:
    colour="balck"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car): #inheritence used
    def __init__ (self,brand):
        self.brand=brand

class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type  

car1=Fortuner("diesel")
print(car1.type)
##print(car1.brand) # we cant acces other constructor object attributes
car1.start()
print(car1.colour) # we can acces, cls attributes, staticmethods

# multiple inheritence
class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class Child(A,B): # taking inheritence of a,b multiple classes(inheritence)
    varC="welcome to classe C"
c1=Child #calling and assigning obj c1 under child calss
print(c1.varA)
print(c1.varB)
print(c1.varC)

