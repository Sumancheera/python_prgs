#class is a blueprint for creating object.
#objects are also called as instance.
class Student:
    school = "10000coders.co" #class attributes
    def __init__(self,name,marks,short): #fullname aslo you can use same name or diffrent
        self.name=name #self.name=fullname
        self.marks=marks #object attributes
        self.short=short 
        print("called obj")
        print(self) #defoult const only self,parameterizes cpnst

s1=Student("suman",97,"s") #
print(s1) #printing the object, it will give address
print(s1.school) # for every student schol is 10k only because defined in class
print(s1.name)
print(s1.marks)

s2=Student("akshayani",99,"ak")
print(Student.school) #class attributes can be print using class name
print(s2.name)
print(s2.marks)
print(s2.short)

# __init__ function or constructor 
# all classes have this init fun, which always exe when obj is being initiated.
# self is ref of current obj and used to access variables of class
