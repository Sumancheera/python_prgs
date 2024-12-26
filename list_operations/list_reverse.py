list=[1,2,3,4,5]
n=len(list)
i=0
while i<n/2:
    first=list[i]
    second=list[n-i-1]
    list[n-i-1]=first
    list[i]=second
    i+=1
print(list)