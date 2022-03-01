import sys

sys.setrecursionlimit(1000000)

def find(x):
  if x == parent[x]:
    return x
  else:
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(x,y):
  x = find(x)
  y = find(y)
  parent[x] = y

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
  command, x, y = map(int, input().split())
  if command==0:
    union(x,y)
  elif command==1:
    if find(x)==find(y):
      print('YES')
    else:
      print('NO')
