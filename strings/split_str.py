#string.split(separator, maxsplit)
txt = "hello, my name is Peter, I am 26 years old" # 2, are ther can become 3 strs
x = txt.split(", ",1) # if we separate
#x = txt.split(",")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")  #x = txt.split("#",1) removes only 1# and makes 2 strs
#split("#",-1) all , deault also all, x = txt.split("#")
print(type(x))
print(x)

#if you use split, end output will be stored in list. #list