list=[1,2,3,4,5]
i=0
while i<len(list): #0<5;1<5;2<5;3<5;4<5
    if(2==list[i]): #false;true;
        i+=1 #before skip we need tp increase #i=2; 
        continue #because after continue exit the if then directly go to the condition check
    print(list[i]) #1;3;4;5
    i+=1 #1;3;4;5
list.insert(5,None)
list.insert(6,6)
print(list)

