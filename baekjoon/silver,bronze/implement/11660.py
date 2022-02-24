n,m = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    dp[i+1][j+1] = matrix[i][j]-dp[i][j+1]+dp[i+1][j]-dp[i][j]

for i in range(m):
  y1, x1, y2, x2 = map(int, input().split())
  print(dp[y2][x2]-dp[y1-1][x2]-dp[y2][x1-1]+dp[y1-1][x1-1])





# for i in range(n):
#   for j in range(n):
#     if i==0 and j==0:
#       continue
#     elif i==0:
#       matrix[i][j]+=matrix[i][j-1]
#     elif j==0:
#       matrix[i][j]+=matrix[i-1][j]
#     else:
#       matrix[i][j]+=matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]

# for _ in range(m):
#   y1, x1, y2, x2 = map(int, input().split())
#   if x1 ==1 and y1 ==1:
#     print(matrix[y2-1][x2-1])
#   elif x1 == 1:
#     print(matrix[y2-1][x2-1]-matrix[y1-2][x2-1])
#   elif y1 == 1:
#     print(matrix[y2-1][x2-1]-matrix[y2-1][x1-2])
#   else:
#     print(matrix[y2-1][x2-1]-matrix[y2-1][x1-2]-matrix[y1-2][x2-1]+matrix[y1-2][x1-2])
