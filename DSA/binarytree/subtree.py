# Definition for a binary tree node.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Solution(object):
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.isIdentical(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def isIdentical(self,root,subRoot):
        if subRoot is None and root is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.data==subRoot.data:
            return self.isIdentical(root.left,subRoot.left) and self.isIdentical(root.right,subRoot.right)
        return False
    
if __name__ == "__main__":
    #creating the tree
    root=Node(2)
    root.left=Node(3)
    root.right=Node(4)
    root.left.left=Node(5)
    root.left.right=Node(6)

    subRoot=Node(3)
    subRoot.left=Node(5)
    subRoot.right=Node(6)

    sol=Solution()
    print(sol.isSubtree(root,subRoot)) #return true/falls.