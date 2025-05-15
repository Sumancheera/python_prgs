class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeInfo:
    def __init__(self, height, diam):
        self.height = height
        self.diam = diam

def diameter(root): #3
    if root is None:
        return TreeInfo(0, 0)

    leftTI = diameter(root.left) #root=1, (2,3)
    rightTI = diameter(root.right) #(1,1)

    myHeight = max(leftTI.height, rightTI.height) + 1 #3

    diam1 = leftTI.diam #3
    diam2 = rightTI.diam #1
    diam3 = leftTI.height + rightTI.height + 1 #2+1+1=4
    
    myDiam = max(diam1, diam2, diam3) #4

    return TreeInfo(myHeight, myDiam) #(3,4)

# Example usage (assuming you have a tree structure built with Node objects):
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree_info = diameter(root)
print("Height:", tree_info.height)
print("Diameter:", tree_info.diam)