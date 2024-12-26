a=int(input("enter starting val ex: 0:"))
b=int(input("enter ending val:"))
flag=0
for i in range(a,b+1):
    if(i==0 or i==1):
        print(i,"is not prime")
        i+=1
        continue
    if(i==2 or i==3):
        print(i,"is primee23")
        i+=1
        continue
    flag=1
    
    for j in range(2,i-1):  # 2 to n-1
        if(i%j==0):
            flag=0
            break
        
    if(flag==1):
        print(i,"is prime")
    else:
        print(i,"not prime")

