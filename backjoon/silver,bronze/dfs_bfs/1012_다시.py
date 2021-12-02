test_case = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(test_case):
  
  m, n, k = map(int, input().split())
  matrix = [[0]*m for _ in range(n)]
  
  for _ in range(k):
    y, x = map(int, input().split())
    matrix[x][y] = 1

  def DFS(i, j):
    stack = [(i, j)]
    count = 0
    while stack:
      x, y = stack.pop()  
      for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n:
          if matrix[nx][ny]==1:
            matrix[x][y]=0
            # print(number)
            stack.append((nx, ny))
            count+=1
            
  for i in range(n):
    for j in range(m):
      if matrix[i][j]==1:
        DFS(i, j)
  for i in matrix:
    print(i)
  