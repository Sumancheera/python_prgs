list=[1,2,3,4,56,6]
i=0
while i<len(list):
    if(2==list[i]):
        i+=1 #before skip we need to increase i, other wise it will stop there.
        continue #because after continue exit the if then directly go to the condition check
    print(list[i])
    i+=1
#