str1="aaababcca"
rem_dup=[]
str2=""
for i in str1:
    if i not in rem_dup:
        rem_dup+=i
print(rem_dup)
for k in rem_dup:
    count=0
    for i in str1:
        if k==i:
            count+=1
    str2 += k+str(count)
print(str2)
    

#2nd method has to be sequency
def compress_string(text):

    if not text:
        return ""

    compressed = ""
    count = 1
    prev_char = text[0]

    for char in text[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed += prev_char + (str(count) if count > 1 else "")
            prev_char = char
            count = 1

    compressed += prev_char + (str(count) if count > 1 else "")  # Add the last character and count

    return compressed

# Example usage:
input_string = "aaabbbcc"
compressed_string = compress_string(input_string)
print(compressed_string)  # Output: a3b3c2

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