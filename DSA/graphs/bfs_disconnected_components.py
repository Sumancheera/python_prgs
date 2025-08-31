from collections import deque
graph1={
    0: [1, 2],
    1: [0, 2],
    2: [0, 1],
    3: [4],
    4: [3]
}           
def bfs(graph,start,visited):
        #visited=set()
        queue=deque([start]) #0,3
        visited.add(start) #0,3
        while queue:
            vertex=queue.popleft() #0,1,2,3,4 #fifo
            print(vertex,end=" ") #0,1,2,3,4
            for neighbor in graph[vertex]:   #3
                if neighbor not in visited:
                    visited.add(neighbor) #imp #0,1,2,4
                    queue.append(neighbor)
        #print()
def dfs(graph,start,visited):
    stack=[start]
    while stack:
        vertex=stack.pop() #stack - first in last out.
        if vertex not in visited:
            visited.add(vertex)
            print(vertex,end=" ")
            for neighbor in graph[vertex]:
                stack.append(neighbor)
def dfs_recursive(graph,start,visited):
    visited.add(start)
    print(start,end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph,neighbor,visited)

visited=set()
v=len(graph1)
all_keys = list(graph1.keys()) # ak did
count=0
for i in all_keys: #0,1,2,3,4
    if i not in visited:
        count+=1
        #bfs(graph1,i,visited) #i=0,3
        #dfs(graph1,i,visited)
        dfs_recursive(graph1,i,visited)
        
print("\nnumber of disconnected components are:\n",count) 
        
