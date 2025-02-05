# fun are objects in python 
#a,b=5,6

#Syntax: lambda arguments : expression
f=lambda a,b:a+b+a**a+b**b
k=lambda a:a*a
print(k(7))
print(type(f))
print(id(f))
print(f(5,6))
results=f(5,6)
print(results)
print(id(results))
print(type(results))

#anonamous function
s1="suman"
s2=lambda s1:s1.upper()
print(s2(s1))

#labda with condition checking 
n = lambda x: "Positive" if x > 0 else "Negative" if x<0 else "zero"
print(n(5))   
print(n(-3))  
print(n(0)) #-ve not printed because it has to satisfy the 2nd if too, we took common task for 1st else and 2nd if.

#Combining lambda with list comprehensions 
li = [lambda arg=x:arg*10 for x in range(1,5)] #[lambda()=10,lambda()=20,lambda()=30,lambda()=40]
for i in li:                                        #0          1             2           3
    print(i())

#Lambda with if-else
check= lambda x: "even" if x%2==0 else "odd"
print(check(4))
print(check(7))