# # to print the max repeated char with its frequency.
str="akshayani"
max_c=0
val=''
for i in range(0,len(str)):
    current_c=1
    for j in range(i+1,len(str)): # this part is to chaeck repaeterd and add ++
        if(str[i]==str[j]): #
            current_c+=1    #
    if current_c>max_c:
        max_c=current_c
        val=str[i]
    #print(" max char:",val,",","freq is:",max_c)  # 
    #max_c=0                                        # not working to pront all the vals 2nd repeated again printing, becaues not able to repeated
print(" max char:",val,",","freq is:",max_c)
