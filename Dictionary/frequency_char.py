# find all the character's frequency of str using dictionary and print in deseeding order
str1 = input("Enter the word: ")
freq = {}
for i in str1:
    if i in freq: #this check it is present or for ordered/un ordered for all.
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
for i in range(len(freq)): #0;1;2;3;4;5;6
    max_c = 0
    max_char = ''
    for key, value in freq.items(): #key:a;k;s;h;y;n;i
        if value > max_c:               #value:3-0;1-0;1-0;1-0;1-0;1-0;1-0
            max_c = value #3;1;1;1;1;1;1
            max_char = key #a;k;s;h;y;n;i
    print(max_char, end = ' : ')
    print(max_c)
    freq[max_char] = 0
print(freq)
