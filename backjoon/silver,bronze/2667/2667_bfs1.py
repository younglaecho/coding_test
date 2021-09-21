N = int(input())

matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
number = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
set_counter = []

def BFS(i, j):
  queue=[(i, j)]
  count = 0
  while queue:
    x, y = queue.pop(0)  
    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if 0 <= nx < N and 0 <= ny < N:
        if matrix[nx][ny]==1 and visited[nx][ny]==0:
          visited[nx][ny]=number
          print(number)
          queue.append((nx, ny))
          count+=1
      # print(queue)
  
  set_counter.append(count)
  # for ele in visited:
  #   print(ele)
  
for i in range(N):
  for j in range(N):
    if matrix[i][j]==1 and visited[i][j]==0:
      BFS(i, j)

print(len(set))
print(set_counter)