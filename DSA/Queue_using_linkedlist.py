class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
    
    #append or add
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    #pop
    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    #print the Queue
    def printll(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
Q1=Queue()
Q1.insertAtEnd(1)
Q1.insertAtEnd(2)
Q1.insertAtEnd(3)
Q1.insertAtEnd(4)

Q1.printll()