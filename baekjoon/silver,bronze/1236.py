n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
row = [False for _ in range(m)]
col = [False for _ in range(n)]

for i in range(n):
  for j in range(m):
    if arr[i][j]=='X':
      row[j]=True
      col[i]=True


def FalseCount (arr) :
  cnt = 0
  for i in arr:
    if not i:
      cnt+=1
  return cnt
  
print(max(FalseCount(col), FalseCount(row)))
