def isprime(n):
    factor=0
    for i in range(1,n+1): # it will take from 1 to n only
        if(n%i==0):
            factor+=1
    if factor==2:
        return True
    else:
        return False
a=int(input("enter starting of range:"))
b=int(input("enter ending val:"))
for i in range(a,b+1):
    if i>1:
        if(isprime(i)):
            print(i,"is prime")
        else:
            print(i,"is not prime")
    else:
        print(i,"not prime//enter val from 2, because 0,1 or neither prime nor composit.")
        