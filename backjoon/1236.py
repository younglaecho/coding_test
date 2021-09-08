n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]
row = [False for _ in range(n)]
col = [False for _ in range(m)]

print(arr)
for i in range(m):
  for j in range(n):
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
