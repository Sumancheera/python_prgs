# create a std cls takes name and 3 subj marks as arguments in constructor. then create a method to print avg.
class Student:
    #name="suman"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(self.name,"avg score is:",sum/3)   

s1=Student("suman",[97,99,98])
s1.avg()
s1.name="akshayani" # we can manupulate the attributes directly. in classes and objects
s1.avg()
