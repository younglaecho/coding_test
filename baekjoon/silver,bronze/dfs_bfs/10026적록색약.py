from collections import deque

n = int(input())

matrix = [list(input()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(i, j, color):
    q = deque()
    q.append([i, j])
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and matrix[nx][ny] == color
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                q.append([nx, ny])


cnt_normal = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, matrix[i][j])
            cnt_normal += 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "G":
            matrix[i][j] = "R"

visited = [[False for _ in range(n)] for _ in range(n)]

cnt_cb = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, matrix[i][j])
            cnt_cb += 1

print(cnt_normal, cnt_cb)
