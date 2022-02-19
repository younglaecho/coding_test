def view_matrix(matrix):
    for arr in matrix:
        strs = ' '.join([str(_) for _ in arr])
        print(strs)
def solution(rows, columns, queries):
    matrix = []
    cnt = 0
    mins = []
    for i in range(rows):
        arr = []
        for j in range(columns):
            cnt+=1
            arr.append(cnt)
        matrix.append(arr)

    for x1, y1, x2,y2 in queries:
        tmp = matrix[x1-1][y1-1]
        minv= tmp
        for i in range(x1-1, x2-1):
            matrix[i][y1-1]= matrix[i+1][y1-1]
            minv = min(matrix[i][y1-1],minv)
            
        for i in range(y1-1,y2-1):
            matrix[x2-1][i] = matrix[x2-1][i+1]
            minv = min(matrix[x2-1][i],minv)
            
        for i in range(x2-1, x1-1, -1):
            matrix[i][y2-1] = matrix[i-1][y2-1]
            minv = min(matrix[i][y2-1],minv)
            
        for i in range(y2-1, y1-1, -1):
            matrix[x1-1][i] = matrix[x1-1][i-1]
            minv = min(matrix[x1-1][i],minv)
        matrix[x1-1][y1] = tmp
        mins.append(minv)
        # view_matrix(matrix)
    return mins