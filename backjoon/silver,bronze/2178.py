from sys import stdin
import time
N,M = map(int, stdin.readline().split())

matrix = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
queue = [(0, 0)]
visited[0][0] = 1

while queue:
  x, y = queue.pop(0)
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < M and 0 <= ny < N:
      if visited[ny][nx] == 0 and matrix[ny][nx] == 1:
        visited[ny][nx] = visited[y][x] +1
        queue.append((nx, ny))
print(visited[N-1][M-1])