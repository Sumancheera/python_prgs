a=2
print(id(a))

# list=[1,2,3,4]
# print(type(list))

# def add(a,b,c=None):
#     return a+b

# result=add("suman","cheera")
# result=add(2,3,4)
# print(result)
# print(type(add))
b=a
print(id(b))
a=3
print(id(a),"a")
print(id(b),"b")