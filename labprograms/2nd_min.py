list=[3,7,4,6,5,1,8]
min=list[0]
min2=list[1]

for i in range(0,len(list)):
    if min >list[i]:
            min2=min     #dont forget this line
            min=list[i]
    elif list[i]>min and list[i]<min2:
            min2=list[i]
print(min,min2)