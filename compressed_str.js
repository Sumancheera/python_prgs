let str="aaabbc"
emp=[]
let str1=""

for(i=0;i<str.length;i++){
    if(!emp.includes(str[i])){
        emp.push(str[i])
    }
}
function countss(k){
    count=0
    // console.log(x)
    for(i=0;i<str.length;i++){
       
        if(k==str[i]){
            count=count+1
        }
    }
    str1=str1+count+k
    
}

for(i of  emp){
  
  countss(i)
}
console.log(str1)