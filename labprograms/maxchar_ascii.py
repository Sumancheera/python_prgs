ak="akshayani" #// akshayani; frqen[97 or a]=3;
frqen=[0]*256 #//ASCII characters range from   /.
maxfreq=0
maxchar=''
for i in range(len(ak)):#{ // i=i+1;
    frqen[ord(ak[i])]+=1   #; //frqen[ak[i]]=frqen[ak[i]]+1;frqen[97]=frqen[97]+1;frqen[97]={1};
    if(frqen[ord(ak[i])]>maxfreq):
        maxfreq=frqen[ord(ak[i])]
        maxchar=ak[i]
print("max char is:",maxchar, end=':')
print("frequency is:",maxfreq)
    #frqen[ord(ak[i])]=0
