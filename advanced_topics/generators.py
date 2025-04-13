def topfive():
    yield 1  #we can use yield keyword to create a generator
    yield 2
    yield 3
    yield 4
    yield 5

for number in topfive():
    print(number)

def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq   #generator
        n+=1
val=topten()
for i in val:
    print(i)

