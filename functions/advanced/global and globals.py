a=10
print(id(a))
b=12
def global_and_globals():
    # global a              #with global, we cant create a local var anymore,it will treate global only.
    # a=15
    # print("inside after global:",a)
# i need one more a local variable but we want to change gloabal var
    x=globals()['a'] #initial a 10
    print("inside:",x)
    print(id(x))
    globals()['a']=18
    a=8
    print(id(a)) #local add
    print("inside, after local:",a)


global_and_globals()
print("outside",a)