# del attibute or object.
#to delete attributes of object or direct object

class Student:
    school="abc school"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student("suman",97)
print(s1)
print(s1.name)
del s1.name #we can delete attibutes of any object
print(s1) 
del s1 #and we can delete any object.
print(s1.marks)
