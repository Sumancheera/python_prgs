str1='suman'
str2="akshayani"
str3="""ak"""
str4="hello.\nhow are you"
print(str4)
str4="hello.\thow are you"
print(str4)

#concatination of strings
str1,str2
print(str1+" "+str2)

#string length
print("string length:",len(str1))   

#how we can asses, but not directly assing 
str="akshayani"
# str[0]="s" #str object does not support item assignment # not allowed
print(str[0])

#slicing
# str[starting_index:ending_index:step]// ending index not included
newstr=str[0:2]
print(newstr) # 0 to 8 index values, last one 9
print(str[0:]) #staring to ending
print(str[:9]) #staring to ending str[:len(str)]
name="suman"[::-1]
print(name,"here i have reversed the str or number")

#negative index
s="suman"
#  s  u  m  a n
# -5 -4 -3 -2 -1   // starts with ending 
print(s[-1]) # prints "n"
print(s[:-1])

#str.endswith("n") returns true if ends with substring
print(s.endswith("man"))
print(s.endswith("n"))

#str.capitalize() // capitalize 1st char.
print(str.capitalize()) #Akshayani
print(str) #akshayani
str=str.capitalize()
print(str) #Akshayani

#str.replace(old,new) #replace all old occarence with new, char or substring
print(str.replace("a","7"))
intro="i am suman, iam learning python with akshayani"
print(intro.replace("python","java"))
print(intro.replace("a","A"))

#str.find("word or char") #returns 1st indext val of 1st occurence
intro="i am suman, iam learning python with akshayani"
print(intro.find("python"))
print(intro[25]) #1st index val

#str.count("am") #counts the occurence of the substring or char
print(intro.count("am"))
print(intro.count("a"))
