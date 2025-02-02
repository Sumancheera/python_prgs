# fun are objects in python 
#a,b=5,6
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
