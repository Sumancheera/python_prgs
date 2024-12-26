list=[1,9,3,7,4,5,6,2,8]
i=0
#max=list[0]
temp=0
while i<len(list):
    j=i+1
    while j<len(list):
        if(list[i]>list[j]): #> assending #<desending
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
        j+=1
    i+=1
print(list)