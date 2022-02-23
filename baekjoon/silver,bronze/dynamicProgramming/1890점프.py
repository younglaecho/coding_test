n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=1

for i in range(n):
  for j in range(n):
    if i == n-1 and j == n-1:
      print(dp[i][j])
      break
    
    if dp[i][j]:
      val = matrix[i][j]
      if i + val < n:
        dp[i+val][j] += dp[i][j]
      if j + val < n:
        dp[i][j+val] += dp[i][j]

print(dp)
    

# def recur(x,y):
#   global cnt
#   if x == n-1 and y == n-1:
#     cnt+=1
#     return

#   if x>=n or y>=n:
#     return
  
#   recur(x+matrix[x][y],y)
#   recur(x,y+matrix[x][y])

# recur(0,0)
# print(cnt)
