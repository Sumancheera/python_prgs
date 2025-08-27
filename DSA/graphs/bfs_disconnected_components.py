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
            vertex=queue.popleft() #0,1,2,3,4
            print(vertex,end=" ") #0,1,2,3,4
            for neighbor in graph[vertex]:   #3
                if neighbor not in visited:
                    visited.add(neighbor) #imp #0,1,2,4
                    queue.append(neighbor)
        #print()

visited=set()
v=len(graph1)
all_keys = list(graph1.keys()) # ak did
count=0
for i in all_keys: #0,1,2,3,4
    if i not in visited:
        count+=1
        bfs(graph1,i,visited) #i=0,3
print("\nnumber of disconnected components are:\n",count) 
        
