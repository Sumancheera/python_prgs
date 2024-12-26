#counting vowels in strings
ak="akshayani"
count=0
for i in range(len(ak)):
    if(ak[i]=='a' or ak[i]=='e'or ak[i]=='i'or ak[i]=='o'or ak[i]=='u'):
        count+=1

print("vowels are:",count)

#printing chars one-by-one usinf for loop
for i in ak: #str #list #tuple.
    print(i)

#tuple count
tuple=("ak",1,2,3,"suman",1,7,"ak","a","k","s","suman")
count=0
for i in range(len(tuple)): #range will give index vals // for i in tuple: in give one-by-one tuple elements
    if("ak"==tuple[i]):
       count+=1
print(count)
    
#tuple copy or duplicate
tuple2=tuple  # use can use this as copy function.
print(tuple2)
print(tuple.index(7))
print(tuple.count("ak"))