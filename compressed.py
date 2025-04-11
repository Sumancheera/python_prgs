#method 3
str1="aaabbcc"
rem_dup=[]
str2=""
for i in str1:
    if i not in rem_dup:
        rem_dup+=i
    
def compressed(k):
    count=0
    global str2    #otherwise it will create another str2 and updates there
    for i in str1:
        if k==i:
            count+=1
    str2+=k+str(count)
    return

for k in rem_dup:
    compressed(k)

print(str2)