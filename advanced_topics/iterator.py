nums=[7,8,9,10]
it=iter(nums)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it)) # you can use any way

#defining own class for iterator
class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=TopTen()
print(next(values)) # it will print 1
print(values.__next__()) #it will print 2nd
for i in values: #then rest will be tracked and print accordingly
    print(i)

