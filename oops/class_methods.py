# class methods- recieves class as attributes
class Person:
    name="anonymous"

    # def changename(self,name):
    #     #self.name=name
    #     #Person.name=name #directly changing class attributes
    #     self.__class__.name=name  #directly changing class attributes
    @classmethod    
    def changename(cls,name):   #cls= Person(class) like self
        cls.name=name

p1=Person() #we can not pass here because fun will tale cls not self
p1.changename("suman") 
print(p1.name,"a")
print(Person.name,"b")

# 1) static method- we cant use or change instance or class methods or attributes
# 2) class methods(class) - if we want to change class attributes
# 3) instance methods(self) - if we need to change object attributes


# @property - decorator - it changes method() to self.method, self.classname() to slef.classname]
# and no need to call again when you chanes the values, it will automatically, takes latest vals

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        #self.percentage=str((self.phy + self.math + self.chem)/3) + "%"
    @property
    def percentage(self):
        return str((self.phy + self.math + self.chem)/3) + "%"

s1=Student(97,99,98)
print(s1.percentage) #init attribute

s1.phy=68
print(s1.percentage) #property decor - fun name as object.attribute
