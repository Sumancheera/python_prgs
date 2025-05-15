class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

#BFS: level order traversal

def bfs(root,k):
    if root is None:
        return
    queue = [root]
    sum=0
    level=0
    while queue:
        level_size=len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            if level==k:
                sum+=node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()
        level+=1
    print("sum is :",sum)


if __name__ == "__main__":
    #creating the tree
    root=Node(2)
    root.left=Node(3)
    root.right=Node(4)
    root.left.left=Node(5)

    bfs(root,2) # calling sum of kth leve in bf