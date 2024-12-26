#wap to ask input names in a list
list1=[]
list1.append(input("enter you 1st name:"))
list1.append(input("enter you 2st name:"))
list1.append(input("enter you 3st name:"))
print(list1)

#wap to check list contains a palindrome of elements(hint: copy() method use )
# [1,2,3,2,1]  # [ 1, "abc", "abc", 1]
list=[1,2,3,2,1] #// ["a", "b", "b","a"]

copyoflist=list.copy()
copyoflist.reverse()

if(copyoflist==list):
    print("palindrome")
else:
    print("not palindrome")

#wap to count A grades in a tuple
tup=("c","b","c","b","a","a","b")
print(tup.count("a"))

#store them to list then sort
list2=["c","b","c","b","a","a","b"]
list2.sort()
print(list2)