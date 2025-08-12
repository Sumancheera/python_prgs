def addedge(src,dest,wt,matrix):
    matrix[src].append([dest,wt])
    matrix[dest].append([src,wt])

def remove_edge(matrix,src,dest,wt):
    if 0<=src<len(matrix) and 0<=dest<len(matrix):
        if [dest,wt] in matrix[src]:
            matrix[src].remove([dest,wt])
            matrix[dest].remove([src,wt])  # remove this if directed
    else:
        print("Edge not found")
def remove_vertex(matrix,vertex):
    if not 0<=vertex<len(matrix):
        print("give vertex up to v value")
        return 
    matrix[vertex].clear() #vertex ah removing vati edges enduku inka.? so ah index clear chyu
    for i in range(len(matrix)):
        if i==vertex:
            continue
        matrix[i][:]=[[neighbor,wt] for neighbor,wt in matrix[i] if neighbor is not vertex]

v=4
matrix=[[] for _ in range(v)] #creating the empty because, list to be appenede as we needed
addedge(0,2,10,matrix)
addedge(1,2,20,matrix)
addedge(1,3,30,matrix)
addedge(2,3,40,matrix)
print(matrix)
remove_edge(matrix,1,2,20)
print(matrix)
remove_vertex(matrix,1)
print(matrix) 