def gcd(n1,n2):
    if n1==0:
        return n2
    elif n2==0:
        return n1
    elif n1==n2:
        return n1
    else:
        if n1>n2:
            small=n2
        elif n2>n1:
            small=n1
    for i in range(1,small+1):
        if n1%i==0 and n2%i==0 :
            gc=i
    return gc

print(gcd(4,9))