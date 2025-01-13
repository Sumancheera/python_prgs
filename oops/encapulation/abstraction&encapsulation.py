# Abstraction- is hiding the implemented details of a class only showing the essential features to users.
class Car:
    def __init__(self):
        self.accel=False
        self.brk=False
        self.clutch=False
    
    def start(self):               # entire details are in the class not outside, hide.
        self.clutch=True
        self.accel=True
        print(" car started..")
    
car1=Car()   #showing only essential car and stating fun, called abstraction.
car1.start()

# encapsulation - wrapping data and funs into unit(oject)

class Account:
    def __init__(self,bal,acc_no):
        self.bal=bal
        self.acc_no=acc_no

    def debit(self,amount):
        self.bal-=amount
        print("your account is debited with",amount)
        print("total bal:",self.bal)

    def credit(self,amount):
        self.bal+=amount
        print("your account is credited with",amount)
        print("total bal:",self.bal) 

    def printing(self):
        print("total bal:",self.bal)

acc1=Account(10000,280601501074)
acc1.debit(100)
acc1.credit(200)
acc1.printing()

