#n1=int(input("enter star:"))
#n2=int(input("enter end:"))

#for i in range(n1,n2+1):
def prime(n1): #n1=0,n1=1,n1=2,n1=3,n1=4,n1=5,n1=6,n1=7,n1=8
    if n1<=1:
        return False
    for j in range(2,n1,+1): # (start,stop,step) j=2,3,4,5,6,7
        if n1%j==0 :
            return False
    else:
        return True
for i in range(0,9,+1):
    if prime(i):  #argument, i=0,i=1,i=2,i=3,i=4,i=5,i=6,i=7,i=8
        print(i,"prime")
    else:
        print(i,"not prime")