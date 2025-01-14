def count_of_prime(N):
    if N<=1:
        return False
    # if N==2 or N==3:
    #     return True
    #stop=int(N//2)
    for i in range(2,int(N**0.5)+1): #if your range is (2,2) or (1,1) it wont execute.
        print("i val",i)
        if N%i==0:
            return False
    return True

def count_primes(n):
    count=0
    for i in range(1,n+1): 
        if count_of_prime(i):
            print("x val:",i)
            count+=1
    return count

n=int(input("enter the num:"))
result=count_primes(n)
print(result)