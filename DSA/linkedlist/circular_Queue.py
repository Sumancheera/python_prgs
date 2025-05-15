#circular Queue in python
class CircularQueue:
    def __init__(self,size):
        self.maxsize=size
        self.queueArray=[0]*size
        self.front=-1
        self.rear=-1

    def isEmpty(self):
        return self.front==-1 and self.rear==-1

    def enqueue(self,item):
        if self.isEmpty():
            print("empty")
            self.front=0
            self.rear=0
            self.queueArray[self.rear]=item #to add 1
        else:
            self.rear=(self.rear+1)%self.maxsize #to increase index vals
            if self.rear==self.front:
                print("Queue is full cannot enqueue.")
                self.rear=(self.rear-1 + self.maxsize)%self.maxsize
            else:
                self.queueArray[self.rear]=item #to ad 2,3,4(3+1)
                print("added")

    def dequeue(self):
        item = -1 # Assuming -1 represents an empty value
        if not self.isEmpty():
            item=self.queueArray[self.front]
            self.queueArray[self.front]=None
            if self.front == self.rear: #if 4==4
                self.front=-1
                self.rear=-1
            else:
                self.front=(self.front+1)%self.maxsize
        else:
            print("Queue is empty. Cannot dequeue.")
        return item

    def peek(self):
        if not self.isEmpty():
            return self.queueArray[self.front]
        else:
            print("Queue is empty. No peek value.")
            return -1 # Assuming -1 represents an empty value

c1=CircularQueue(5)

c1.enqueue(1)
c1.enqueue(2)
c1.enqueue(3)
print(c1.peek())
c1.enqueue(4)
c1.enqueue(5)
c1.dequeue()
c1.dequeue()
c1.enqueue(6)
print(c1.peek())
c1.enqueue(7)
print(c1.queueArray)
print("front:",c1.front,"rear:",c1.rear)