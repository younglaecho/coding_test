n = int(input())


def a(x):
    return 1 if x == "Y" else 0


matrix = [list(map(a, list(input()))) for _ in range(n)]

# print(matrix)

result = []
for i in range(n):
    visited = [False] * (n)
    for j in range(n):
        if matrix[i][j] == 1:
            visited[j] = True
            for k in range(n):
                if matrix[j][k] == 1:
                    visited[k] = True
    if visited[i]:
        result.append(sum(visited) - 1)
    else:
        result.append(sum(visited))
print(max(result))
# def dfs(matrix, i):
#     visited = [False] * (n)
#     depth = 0
#     stack = [(i, depth)]
#     cnt = 0
#     while stack:
#         value, depth = stack.pop()
#         if not visited[value] and depth <= 2:
#             cnt += 1
#             visited[value] = True
#             for c in range(len(matrix[value]) - 1, -1, -1):
#                 if matrix[value][c] == 1 and not visited[c]:
#                     stack.append((c, depth + 1))
#     return cnt


# result = []
# for i in range(n):
#     # print(visited)
#     result.append(dfs(matrix, i))
# # print(result)
# print(max(result) - 1)
