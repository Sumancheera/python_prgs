class Dog:
    def __init__(self,name,breed,age):
        self.name=name        #public attribute
        self._breed=breed     #protected attributr
        self.__age=age        #private attribute
    #public method to print within the calss everyone can call
    def get_info(self):
        return f"name:{self.name}, breed:{self._breed},Age:{self.__age}"
    
    #getter and setter for private attributes 
    def get_age(self):
        return self.__age
    
    def set_age(self,age):  #age, __age both are diffrent attributes
        if age >0:
            self.__age=age
        else: print("invalid age")

#creating object
dog1=Dog("buddy","labrador",3)
print(dog1.name) # Accessing public member
print(dog1._breed)    # Accessing protected member,# Accessible but discouraged outside the class
print(dog1.get_age())  # Accessing private member using getter
dog1.set_age(6)  # Modifying private member using setter
print(dog1.get_info())


#python prm to show getter() and setter() in normal fun.
class Person:
    def __init__(self,age=0): #because we have assigned the defoult parameter
        self._age=age
    #getter method
    def get_age(self):
        return self._age
    #setter method()
    def set_age(self,age):
        self._age=age   # age, _age diffrent
    
raj=Person() #here we are not passing any val
raj.set_age(18)
print(raj.get_age())
print(raj._age)

#using getter and setter by property() fun
class Persons:
    # def __init__(self):
    #     self._age=0          #anyway in baground init fun will be executed
    def get_age(self):
        print("getter is called")
        return self._age
    def set_age(self,age):
        print("setter is called")
        self._age=age
    def del_age(self):
        del self._age
    age=property(get_age,set_age,del_age)

maruthi=Persons()
maruthi.age=19 #it triggets the set fun,because of assigning 19 val
print(maruthi.age) #printed 19 because returned 19


#python prg showing use of @property decorator
class People:
    def __init__(self):
        self._ages=0
    @property
    def ages(self): #getter fun
        print("getter fun is called")
        return self._ages
    @ages.setter
    def ages(self,a):
        if a<18:
            raise ValueError("age is below 18y")
        print("setter method is called")
        self._ages=a

suman=People()
suman.ages=20
print(suman.ages)






