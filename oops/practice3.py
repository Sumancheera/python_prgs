#employee detils using oops
class Employee:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    def showdetails(self):
        print("role is:",self.role)
        print("dep is:",self.dep)
        print("salary is:",self.salary)

class Engineer(Employee):
    def __init__(self,name,age,role,dep,salary): #we can remove inhereted attributes and add drectly in 17th line
        self.name=name
        self.age=age
        super().__init__(role,dep,salary)
        #super().__init__("accountent","finance",25000)
    def showdetails(self):
        print("name is:",self.name)
        print("age is:",self.age)
        print("role is:",self.role)
        print("dep is:",self.dep)
        print("salary is:",self.salary)

# e1=Employee("developer","it",50000)
# e1.showdetails()
emp1=Engineer("akshayani",21,"software developer","IT",50000)
emp1.showdetails()
