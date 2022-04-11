from collections import deque

m, n, h = map(int, input().split())
matrix = []

for i in range(h):
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))
    matrix.append(arr)

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

queue = deque()
cnt = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    z, y, x = queue.popleft()
    for k in range(6):
        nx = x + dx[k]
        ny = y + dy[k]
        nz = z + dz[k]
        if 0 <= ny < n and 0 <= nx < m and 0 <= nz < h:
            if matrix[nz][ny][nx] == 0:
                matrix[nz][ny][nx] = matrix[z][y][x] + 1
                queue.append((nz, ny, nx))

Max = 0
breaked = False
for i in matrix:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                breaked = True
                break
            else:
                Max = max(Max, k)
        if breaked:
            break
    if breaked:
        break

if not breaked:
    print(Max - 1)
