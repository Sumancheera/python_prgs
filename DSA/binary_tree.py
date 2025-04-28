from collections import deque
from math import* 
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
# in-order DFS: left,root,right
def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data, end=" ")
    in_order_dfs(node.right)

#pre-order DFS: root,left,right
def pre_order_dfs(node):
    if node is None:
        return
    print(node.data, end=' ')
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

#post-order DFS: left,right,root
def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.data, end=' ')

#BFS: level order traversal
def bfs(root):
    if root is None:
        return
    queue = [root]
    while queue:
        level_size=len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

def countNodes(root):
    if root ==None:
        return 0
    leftcount=countNodes(root.left)
    rightcount=countNodes(root.right)
    return leftcount+rightcount+1

def sumNodes(root):
    if root ==None:
        return 0
    leftcount=sumNodes(root.left)
    rightcount=sumNodes(root.right)
    return leftcount+rightcount+root.data

def hightoftree(root):
    if root ==None:
        return 0
    lefthight=hightoftree(root.left)
    righthight=hightoftree(root.right)
    return max(lefthight,righthight)+1

# Function to insert a new node in the binary tree
def insert(root, key):
    if root is None:
        return Node(key)
    # Create a queue for level order traversal
    queue = deque([root])
    while queue:
        temp = queue.popleft()

        # If left child is empty, insert the new node here
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)
        # If right child is empty, insert the new node here
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)
    return root
        
if __name__ == "__main__":
    #creating the tree
    root=Node(2)
    root.left=Node(3)
    root.right=Node(4)
    root.left.left=Node(5)

    root = insert(root, 6)  #insert code

    print("In-order DFS: ", end='')
    in_order_dfs(root)
    print("\nPre-order DFS: ", end='')
    pre_order_dfs(root)
    print("\nPost-order DFS: ", end='')
    post_order_dfs(root)
    print("\nLevel order: ", end='')
    bfs(root)
    print("number of nodes is:")
    count=countNodes(root)
    print(count)
    print("sum of nodes is:")
    sum=sumNodes(root)
    print(sum)
    hight=hightoftree(root)
    print("hight of nodes is:")
    print(hight)
    