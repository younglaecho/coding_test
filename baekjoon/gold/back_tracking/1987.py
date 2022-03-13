n, m = map(int, input().split())

matrix = [list(input()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
result = 0
visited_alp = {matrix[0][0]}


def dfs(x, y, depth):
    global result
    result = max(result, depth)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not matrix[ny][nx] in visited_alp:
            visited_alp.add(matrix[ny][nx])
            dfs(nx, ny, depth+1)
            visited_alp.remove(matrix[ny][nx])


dfs(0, 0, 1)
print(result)
