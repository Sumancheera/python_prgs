# static methods dont use self parameters, (so works at class level only)
class Student:
    def __init__(self,name):
        self.name=name

    @staticmethod  #decorator
    def college():
        print("ABC college")

s1=Student("suman")
s1.college() #we need object to print,becase that fun is in class.
s2=Student("ak")
s2.college() #to print every time for all the objects