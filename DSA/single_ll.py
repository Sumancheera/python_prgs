#single linked list
#creating node class to create a node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#creating a linkedlist class
class linkedlist:
    def __init__(self):
        self.head=None 
    #method to add a node at begining of ll
    def insertAtBegining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    #method to add at any index,from o to n-1
    def insertAtIndex(self,data,index):
        if index==0:
            self.insertAtBegining(data)
            return
        position=0
        current_node=self.head
        while self.head is not None and position+1 != index:
            position +=1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")
    #method to add a new node at the end of ll
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    #update nodeat given position
    def updateNode(self,val,index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position +=1
            current_node = current_node.next
        
        if current_node is not None:
            current_node.data = val
        else:
            print("index not present")
        
    #method to remove first node of ll
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next
    #method to remove last node in ll
    def remove_last_node(self):
        if self.head is None:
            return
        #if theres only one node
        if self.head.next is None:
            self.head = None
            return
        #traverse to second last node
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    #method to remove node at a given index
    def remove_at_index(self,index):
        if self.head is None:
            return
        if index == 0:
            self.remove_first_node
        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position +1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("index not present")
    #method to remove a node from linked list by its data
    def remove_node(self,data):
        current_node = self.head

        #if node to be removed is head node
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return
        #traverse and find node with matching data
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        #if the data wan not found
        print("node with the given data not found")
    #print the size of the linked list
    def sizeofll(self):
        size = 0
        current_node = self.head
        while current_node:
            size+=1
            current_node = current_node.next
        return size
    #print the linked list
    def printll(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

#create a new lisked list
llist = linkedlist()

#add nodes to ll
llist.insertAtBegining(1)
#llist.insertAtBegining(2)
llist.insertAtEnd(3)
llist.insertAtIndex(7,2)
llist.insertAtEnd(4)
llist.insertAtEnd(5)
llist.insertAtEnd(6)
llist.printll()

#remove nodes
print("removing first node:")
llist.remove_first_node()
print("\nremoving last node:")
llist.remove_last_node()
print("\nRemove Node at Index 1:")
llist.remove_at_index(1)

# print the linked list after all removals
print("\nLinked list after removing a node:")
llist.printll()
print("\nUpdate node Value at Index 0:")
llist.updateNode('z', 0)
llist.printll()
print("\nSize of linked list:", llist.sizeofll())