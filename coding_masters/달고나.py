n, m = map(int, input().split())

matrix = [list(input()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


def show(matrix):
    for i in matrix:
        for j in i:
            print("{:1}".format(j), end="")
        print()


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(i, j):
    stack = [(j, i)]
    visited[j][i] = True

    while stack:
        y, x = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if matrix[ny][nx] == "0" and not visited[ny][nx]:
                    visited[ny][nx] = True
                    stack.append((ny, nx))


cnt = 0
for i in range(m):
    for j in range(n):
        if visited[j][i] == False and matrix[j][i] == "0":
            bfs(i, j)
            cnt += 1

# print("-" * 50)
# show(visited)

print(cnt)
