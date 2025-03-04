class Student:
    school = "10000coders.co" #class attributes
    def __init__(self,name,marks): #
        self.name=name #self.name=fullname
        self.marks=marks #object attributes
    

s1=Student("suman",97) #
ak=s1
print(s1)
print(ak.name)