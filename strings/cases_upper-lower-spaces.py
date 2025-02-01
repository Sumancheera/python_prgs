#str.upper() # it will convert total string to upper case
intro= "i am suman,iam learning python with akshayani"
print(intro.upper()) # I AM SUMAN, IAM LEARNING PYTHON WITH AKSHAYANI
s="SUMAN"
print(s.lower())

# Input : string = 'GeeksforGeeks is a computer Science portal for Geeks'
# Output : Uppercase - 4
#          Lowercase - 41
#          spaces - 7
#          gEEKSFORGEEKS IS A COMPUTER sCIENCE PORTAL FOR gEEKS
string = 'GeeksforGeeks is a computer Science portal for Geeks'
newstring = '' 
count1 = 0
count2 = 0
count3 = 0

for a in string: 
	# converting to uppercase. 
	if (a.isupper()) == True: 
		count1 += 1
		newstring += (a.lower()) 
	# converting to lowercase. 
	elif (a.islower()) == True: 
		count2 += 1
		newstring += (a.upper()) 

	# adding it to the new string as it is. 
	elif (a.isspace()) == True: 
		count3 += 1
		newstring += a 
print("In original String : ") 
print("Uppercase -", count1) 
print("Lowercase -", count2) 
print("Spaces -", count3) 
print("After changing cases:") 
print(newstring) 
