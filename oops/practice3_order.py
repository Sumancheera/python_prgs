#order1> order2
# # __gt__()
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,order2):
        return self.price > order2.price #if we put > sysmbol it has to be order1>order2 other wise false
    def __lt__(self,order2):
        return self.price<order2.price
    
order1=Order("orange",25)
order2=Order("apple",22)
print(order1>order2) #reruns true/false
print(order1<order2)
         