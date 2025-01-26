# in python neither of it we use 
# like pass by val, we can change variable name but it uses same memory address-aliasing like.
# because int,str are immutable types
#there are 
#You can use mutable types(list,dictionary) or the ctypes module to achieve pointer-like functionality when necessary.
#Python doesn't have explicit pointers, but everything is a reference to an object

def immutable_update(x): #aliasing but pointing to same momory locatio
    print(id(x))
    x=8           # creating one more object for x variable because int is immutable. memory diff.
    print("x val:",x)
    print(id(x))

a=10
print(id(a))
immutable_update(a)
print("a val:",a) # after func call it wont change, because x is now a new object/memory location.

# to get pass by ref like fee - use mutables data types like list and dictionary.
def immutable_update(lst): 
    print(id(lst))
    lst[0]=8           
    print("lst val:",lst)
    print(id(lst))

list=[10,20,30]
print(id(list))
immutable_update(list)
print("list :",list)
