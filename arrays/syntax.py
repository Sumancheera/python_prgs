import array as arr # only impoting array defination as arr
from array import * #inporting all the func
# i signed, +-1
# u conic code char
vals=array('i',[5,4,-8,2,9])
print(vals.buffer_info()) #(address,size)
vals.reverse()
vals.append(1)
print(vals)
char=array('u',['q','w','e','r'])
print(type(char),char)
newarray=array(vals.typecode,(a for a in vals)) # we can asign a*a also, or a+a, a-1, anything
for e in newarray:
    print(e)