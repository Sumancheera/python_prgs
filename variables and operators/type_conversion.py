#type conversion or implicit happens automatically
a,b=2,3.5
sum=a+b
print(sum) #sum printed in float, type converted

#type castting or explicit conversion
x,y=2,"3"
x,y=2,int("3")
z=int(y)
total=x+y
print(total)
print(x+z)
# we cant convert str to float or int
#but we can convert int or float to str
val1,val2=True,False
val3=str(val1)
print(val1) #we can convert bool to str 