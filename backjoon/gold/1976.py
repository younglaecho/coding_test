def find(x):
  if x == parent[x]:
    return x
  else:
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)

  parent[y] = x

n = int(input())
m = int(input())
parent = []

for i in range(n+1):
  parent.append(i)

for i in range(1,n+1):
  arr = list(map(int,input().split()))
  cnt = 1
  for j in range(n):
    if arr[j]==1:
      union(i, cnt)
    cnt+=1
    
cities = list(map(int, input().split()))
prev = find(cities[0])
for i in cities: 
  if find(i) != prev:
    print('NO')
    break
  prev = find(i)
else:
  print('YES')