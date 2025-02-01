#n1=int(input("enter star:"))
#n2=int(input("enter end:"))

#for i in range(n1,n2+1):
def prime(n1):
    if n1<=1:
        return False
    for j in range(2,n1):
        if n1%j==0 :
            return False
    else:
        return True
for i in range(0,9):
    if prime(i):
        print(i,"prime")
    else:
        print(i,"not prime")