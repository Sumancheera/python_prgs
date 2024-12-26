list=[3,7,4,6,5,1,8]
max=list[0]
max2=list[1]

for i in range(0,len(list)):
    if max<list[i]:
            max2=max     #dont forget this line
            max=list[i]
    elif list[i]<max and list[i]>max2:
            max2=list[i]
print(max,max2)