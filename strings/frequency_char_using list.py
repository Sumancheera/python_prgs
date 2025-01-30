s=input("enter the string:")
list=[]
for i in s:
    if i not in list:
        list.append(i)
for i in list:
   # if s.count(i)>1:
        print(i,":",s.count(i))