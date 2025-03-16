
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def add_at_beg(head,data):
    new_node=Node(data)
    new_node.next=head
    return new_node

def add_at_end(head,data):
    if head is None:
        head=add_at_beg(head,data)
        return head
    new_node=Node(data)
    current= head
    while current.next:
        current=current.next
    current.next=new_node
    return head
def add_at_pos(head,index,data):
    if index==0: #for 1st node
        return add_at_beg(head,data)
    else:
        current=head
        pos=0
        while current is not None and  pos+1 !=index: #this is for 3rd node on wards
            pos+=1
            current=current.next
        if current is not None: #this is for 2st node
            new_node=Node(data)
            new_node.next=current.next
            current.next=new_node
        else:
            print("invalid pos")
        
def del_at_beg(head):
    current=head
    current=current.next
    return current

def del_at_end(head):
    if head==None:
        print("empty list")
        return head
    if head.next==None:
        head=None
        return head
    current=head
    while current.next!=None and current.next.next is not None:
        current=current.next
    current.next=None
    return head
def del_at_pos(head,index):
    if head is None:
        print("list is empty")
    if index==0:
        return del_at_beg(head)
    else:
        pos=0
        current=head
        while current!=None and current.next is not None and pos+1 !=index:
            pos+=1
            current=current.next
        if current!=None and current.next is not None:
            current.next=current.next.next
        else:
            print("index not present")
    return head
def printll(head):
    while head:
        print(head.data,end="->")
        head=head.next
    print("end")

head=None
head=add_at_beg(head,1)
head=add_at_beg(head,2)
head=add_at_beg(head,3)
head=add_at_end(head,4)
head=add_at_pos(head,0,5)
printll(head)
head=del_at_beg(head)
# head=del_at_end(head)
head=del_at_pos(head,1)

# del_at_end(head)
printll(head)