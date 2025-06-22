
class Node:
    def __init__(self,data):
            self.data=data
            self.left=None
            self.right=None
class BST:
    def __init__(self):
         self.root=None
    
    #recursive fun to insert nodes into BST
    def insert(self,root,data): #everytime we should use self.root,self.root.right but we are just using root and created utility method
        # we cant use self.root=self
        if root is None:
            return Node(data) # If tree/subtree is empty, create a new node
        #recursivley insert in the left subtree if the data is smaller 
        if data<root.data:
             root.left=self.insert(root.left,data)
        elif data> root.data: #
             root.right=self.insert(root.right,data)
        return root #this is to return unchanged root.
    
    def insert_node(self,data): # Utility method to insert a node
        self.root=self.insert(self.root,data)
    #root=insert(root,2) # here ill get root not defined for calling fun,
    def inorder(self,root):
         if root:
              self.inorder(root.left)
              print(root.data,end=" ")
              self.inorder(root.right)
    def inorder_trversal(self):  # Utility method to start inorder traversal from root
        self.inorder(self.root)
        print() #for new line for next things or after printing
    def delete(self,root,data):
        if root is None:
             return root
        if data<root.data:
            root.left=self.delete(root.left,data)
        elif data>root.data:
             root.right=self.delete(root.right,data) 
        else:
            if root.left and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            inordersuccessor=self.find_min(root.right)
            root.data=inordersuccessor.data 
            root.right=self.delete(root.right,inordersuccessor.data)
        return root # Return the unchanged root
    def find_min(self,root):
        while root.left:
            root = root.left # Go as far left as possible
        return root
    def delete_node(self,data): #utility function for delete
         self.root=self.delete(self.root,data)

    def search(self,root,data):
        if root is None:
             return False
        if root.data>data:
             return self.search(root.left,data)
        elif root.data is data:
            return True
        else:
            return self.search(root.right,data)
    def search_node(self,data):
        return self.search(self.root,data)
    def printinrange(self,root,x,y): #8;5;6;5.5;7;10;9;11;9.5
        if root is None:
            return #this is the problem why we are not assigning this fun call to anything in utility, root will become zero.
        if root.data>=x and root.data<=y: #8>=6;6>=6;10>=6&&<=10;9>=10;9.5>6&&<=10;
            self.printinrange(root.left,x,y) #8.left(5);6.left(5.5);7.left(none);10.left(9);9.left(none);9.5.left(none)
            print(root.data,end=" ") #6,7,8,9,10,9.5
            self.printinrange(root.right,x,y)#6.right(7);7.right(none);8.right(10);9.right(none);10.right(11);9.5.right(none)
        elif root.data<x: #5<6;5.5<6;  
            self.printinrange(root.right,x,y) #5.right(6);5.5.right(none);  
        else:
            self.printinrange(root.left,x,y)#11.left(9.5);   
    def print_range(self,x,y): # utility fun for printin range
        return self.printinrange(self.root,x,y) 
    def printpath(self,root,list):
        if root is None:
            return
        list.append(root.data)
        if root.left is None and root.right is None:
            print(list)
        else:
            self.printpath(root.left,list)
            self.printpath(root.right,list)
        list.pop() #this is for removing the last element from the list
    def print_paths(self,list): #utility fun
        return self.printpath(self.root,list)

#creating a new bst instace 
bst=BST()

# bst.root=Node(8) 
# bst.root.left=Node(5) 
# bst.root.left.left=Node(3) 
# bst.root.left.right=Node(6) 
# bst.root.left.right.left=Node(5.5) 
# bst.root.left.right.left.left=Node(5.2) 
# bst.root.left.right.right=Node(7)              #for print in range: 7 8 9 10 9.5 you will get this order
# bst.root.right=Node(10)                            #because the tree forms diffrently
# bst.root.right.left=Node(9) 
# bst.root.right.right=Node(11) 
# bst.root.right.right.left=Node(9.5) 
# bst.root.right.right.right=Node(14) 
# bst.root.right.right.right.left=Node(13) 
# bst.root.right.right.right.right=Node(15) 
#insert nodes into the bst
nodes=[8,5,6,3,5.5,5.2,7,10,9,11,9.5,14,13,15]
for i in nodes:
    bst.insert_node(i) # def insert_node(self,data): # fro this tree 7 8 9 9.5 10 you will get this order,because its adds in level order and with bst rules.
# bst.insert_node(8)# bst.insert_node(5)# bst.insert_node(6)# bst.insert_node(3)# bst.insert_node(5.5)# bst.insert_node(5.2)# bst.insert_node(7)
# bst.insert_node(10)# bst.insert_node(9)# bst.insert_node(11)# bst.insert_node(9.5)# bst.insert_node(14)# bst.insert_node(13) # bst.insert_node(15)
bst.inorder_trversal() # to print in inorder.
list=[]
bst.print_paths(list)

bst.delete_node(14) #delete
bst.inorder_trversal()
bst.delete_node(6)
bst.inorder_trversal()
found=bst.search_node(11)
if found:
    print("found the data:",found)
else:
    print("not found the data:",found)
print("root is:",bst.root.data)

bst.print_range(6,10) 
