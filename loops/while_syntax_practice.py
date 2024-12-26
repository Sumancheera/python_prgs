#while loop
#while condition:
    #do this work
    #i++

#print num from 1 to 100
i=1
while i<=10:
    print(i)
    i+=1
print("end of the prg")
# #print num from 100 to 1
i=10
while i>=1: #stoping statment or condition, if condition false it stops.
    print(i)
    i-=1
print("end of the prg")

# #multiplication table of a num n
n=int(input("enter the table:"))
i=1
while i<=10:
    print(i*n)
    i+=1

# #print the list elements using a loop
list=[43,6,54,65,77,2,7,87,8,25,9]
i=0
while i<=len(list)-1:
    print(list[i])  #travers
    i+=1

# #break and continue// skipp
# #if you find 2 in list brak the loop
i=0
while i<len(list):
    if(2==list[i]):
        print("found at index:",i)
        break
    i+=1

#continu if you want anything to skip in the iteration
i=0
while i<len(list):
    if(2==list[i]):
        i+=1 #before skip we need to increase i
        continue #because after continue exit the if then directly go to the condition check
    print(list[i])
    i+=1
#