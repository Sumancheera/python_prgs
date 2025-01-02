# static methods dont use self parameters, (so works at class level only)
class Student:
    @staticmethod  #decorator
    def college():
        print("ABC college")

s1=Student()
s1.college() #we need object to print,becase that fun is in class.