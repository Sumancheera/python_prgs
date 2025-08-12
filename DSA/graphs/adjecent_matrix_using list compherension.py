def addedge(i,j,wt):
    matrix[i][j]=wt
    matrix[j][i]=wt    # put 1 if it is un-weighted 
    # return matrix
v=4
matrix=[[0]*v for _ in range(v)]
addedge(0,2,10)
addedge(1,2,20)
addedge(1,3,30)
addedge(2,3,40)
print(matrix)

