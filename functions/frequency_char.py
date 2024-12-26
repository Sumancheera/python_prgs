#def print_freq(list):
    
def  cal_freq(str):
    list=[0]*26
    for i in range(len(str)):
        if str[i]>='a' and str[i]<='z':
            list[ord(str[i])-ord('a')]+=1
        else:
            list[ord(str[i])-ord('A')]+=1
    #print_freq(list)
    for j in range(0,26):     
        if(list[j]!=0):
            if str[i]>='a' and str[i]<='z':
                print("max char:",chr(j+ord('a')), end =':')
            else:
                print("max char:",chr(j+ord('A')), end =':')
            print(list[j])

str="AKSHAYANI"
cal_freq(str)
