class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Circular_ll:
    def __init__(self):
        self.last=None
    
    def print_list(self):
        if self.last is None:
            return
        head=self.last.next
        while True:
            print(head.data,end="->")
            head=head.next
            if head==self.last.next:
                print("last")
                return
    def insert_at_beg(self,data) :
        new_node=Node(data)
        new_node.next=self.last.next
        self.last.next=new_node
        return
    def insert_at_end(self,data):
        new_node=Node(data)
        new_node.next=self.last.next
        self.last.next=new_node
        self.last=new_node
        return 
    def insert_at_pos(self,pos,data):
        if pos == 0:
            self.insert_at_beg(self,data)
            return 
    #Create a new node with the given data
        new_node = Node(data)
    # curr will point to head initially
        curr = self.last.next

    # Traverse the list to find the insertion point
        for i in range(1, pos):
            curr = curr.next
        # If position is out of bounds
            if curr == self.last.next:
                print("Invalid position!")
                return 
        # Insert the new node at the desired position
        new_node.next = curr.next
        curr.next = new_node
        # Update last if the new node is inserted at the end
        if curr == self.last:
            self.last = new_node
        return
    def del_at_beg(self):
        if self.last is None:
            print("empty linked list")
            return None
        curr=self.last.next
        if curr == self.last:
            self.last = None
        else:
            self.last.next=curr.next
        return
    def del_at_end(self):
        curr=self.last.next

        while(curr.next !=self.last):
            curr=curr.next
        curr.next=self.last.next
        self.last=curr
        return 
    def del_at_pos(self,pos):
        if pos == 0:
            self.del_at_beg(self)
            return
        curr=self.last.next
        for i in range(1,pos):
            curr=curr.next
            if curr  == self.last:
                print("invalid ")
                #self.last=curr
                return 
        curr.next=curr.next.next
        self.last=curr
        return 

first=Node(1)
first.next=Node(2)
first.next.next=Node(3)
first.next.next.next=Node(4)
circular_ll=Circular_ll()
circular_ll.last=first.next.next.next
circular_ll.last.next=first
circular_ll.insert_at_beg(0)
circular_ll.insert_at_end(5)

circular_ll.insert_at_pos(6,6)
circular_ll.print_list()
circular_ll.del_at_beg()
circular_ll.del_at_end()
print(circular_ll.last.data)

circular_ll.print_list()
circular_ll.del_at_pos(4)
circular_ll.print_list()
print(circular_ll.last.data)
circular_ll.print_list()

