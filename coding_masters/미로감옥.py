from collections import deque

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]
dist[0][0] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
queue.append((0, 0))
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if dist[ny][nx] == 0 and matrix[ny][nx] == "1":
                dist[ny][nx] = dist[y][x] + 1
                queue.append((nx, ny))


print(dist[-1][-1])
