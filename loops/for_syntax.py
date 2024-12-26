#syntax
#for i in range(start?,stop,step?): #? are optional takes from starting like 0 then step defoult +1;
# it will take index not list values
original_list=[1,2,3,4,5]
for i in range(len(original_list)):
    print(i)

ak=[1,4,2,3,1,4,123,4,31,4,5]
x=4
for i in range(len(ak)):
    if(ak[i]==x):
        print("found at:",i)

# i-- decreacing order
for i in range(10,0,-1):
    print(i)
    
# pass 
for el in range(10): 
    pass              #place holder of future code.
