# n, m = map(int, input().split())

# matrix = [input() for _ in range(n)]
# result = []
# for i in range(10):
#   for j in range(len(matrix)):
#     if matrix[j].count(str(i)) > 1:
#       start = matrix[j].find(str(i))
#       last = matrix[j].rfind(str(i))
#       gap = last-start
#       for k in range(1, gap):
#         if (j+k)<n and int(matrix[j][start+k])==i and int(matrix[j+k][start])==i and int(matrix[j+k][start+k])==i:
#           result.append((k+1)**2)
#       # print(i,j,start,last)
#       # print(j, result)
# if result:
#   print(max(result))
# else:
#   print(1)

n, m = map(int, input().split())

matrix = [input() for _ in range(n)]
result = []
check = min(n, m)
answer = 0
for i in range(n):
    for j in range(m):
        for k in range(check):
            if ((i + k) < n) and ((j + k) < m) and (matrix[i][j] == matrix[i][j + k] == matrix[i + k][j] == matrix[i + k][j + k]):
              result.append((k+1)**2)
if result:
  print(max(result))
else:
  print(1)