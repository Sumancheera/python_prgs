# delete module 
#like code libraries od others we can import 
import os
#os.remove("c:/Users/HP/Desktop/python programs/files/delete.txt")
# deleted the txt file 

#practice questions
with open ("c:/Users/HP/Desktop/python programs/files/practice.txt","r") as f:
    #f.write("i am going to replace a few a data\n i am learning python")
    data=f.read()
    newdata=data.replace("python","java")
with open ("c:/Users/HP/Desktop/python programs/files/practice.txt","w") as f:
    f.write(newdata)

#def 
#find learning word exist or not.
word="learning"
with open ("c:/Users/HP/Desktop/python programs/files/practice.txt","r") as f:
    data=f.read()
    if  data.find(word)!= -1: # not found
        print("found")
    else:
        print("not found")

# find the line num of learning word, first occured
def find_line(): 
    data=True
    lineno=1
    with open ("c:/Users/HP/Desktop/python programs/files/practice.txt","r") as f:
        while True: # stops when false- finds last empty line/space
            data=f.readline()
            if word in data: #check for word 
                print(lineno)
                return #or break  #used for, it may give word in 2nd line so preventing, first word
            lineno+=1 
    return -1 # if not found anything 
    
print(find_line)

#file containing nums separated with commas, print count of even nums
with open("c:/Users/HP/Desktop/python programs/files/nums.txt","r") as f:
    data=f.read() # data is in string 
    print(data)
    #need to seperate individual nums #then parse, typecaste to int.
    # num=''
    # for i in range(len(data)):
    #     if data[i]==',':
    #         print(int(num))
    #         num=''
    #     else:
    #         num+=data[i]
    count=0
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
    print(count)
    #string.split(separator, maxsplit)
    #separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
#maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
