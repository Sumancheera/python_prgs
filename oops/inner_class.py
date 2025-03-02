class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap= self.Laptop() #init and classname() both are same
    def show(self):
        print(self.name,self.rollno)
        self.lap.show() 

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.ram=16
        def show(self):
            print(self.brand,self.ram)
s1=Student("suman",517)
s2=Student("akshayani",510)
s1.show(),s2.show()
lap=Student.Laptop() #in inner class you can pass details but you can give direct val to attibutes in calss 2
s1.lap.show()
print(s2.lap.brand)