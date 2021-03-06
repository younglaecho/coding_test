N = int(input())

matrix = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
set_counter = []
number = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def BFS(x0, y0):
  cnt = 1
  queue = [(x0,y0)]
  while queue:
    x, y = queue.pop(0)
    visited[x][y] = number
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        if visited[nx][ny]==0 and matrix[nx][ny]==1:
          visited[nx][ny] = number
          queue.append((nx,ny))
          cnt+=1

  set_counter.append(cnt)

for i in range(N):
  for j in range(N):
    if matrix[i][j] == 1 and visited[i][j]==0:
      number += 1
      BFS(i, j)


print(number)
set_counter.sort()
for i in set_counter:
  print(i)

