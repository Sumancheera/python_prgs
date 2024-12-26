a=0
b=1
c=a+b
n=int(input("enter the num:"))
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c
    
