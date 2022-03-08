# n = int(input())

# matrix = [list(map(int, input().split())) for _ in range(n)]
# result = [[0 for _ in range(n)] for _ in range(n)]
# visited = [False] * (n + 1)


# def dfs(matrix, i):
#     stack = [i]
#     while stack:
#         value = stack.pop()
#         if not visited[value]:
#             visited[value] = True
#             for c in range(len(matrix[value]) - 1, -1, -1):
#                 if matrix[value][c] == 1 and not visited[c]:
#                     stack.append(c)
#                     result[i][c] = 1
#                 elif matrix[value][c] == 1 and i == c:
#                     result[i][i] = 1


# for i in range(n):
#     dfs(matrix, i)
#     visited = [False] * (n + 1)

# for i in result:
#     print(" ".join(list(map(str, i))))


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][k] = 1
                matrix[i][j] = 1
                matrix[k][j] = 1

for i in matrix:
    print(" ".join(list(map(str, i))))
