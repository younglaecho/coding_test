import copy
from re import S
m, n = map(int, input().split())

def test(matrix, i, j):
  global m
  global n
  if i-1>=0 and matrix[i-1][j] == 0:
    matrix[i-1][j]= 1
  if i+1<n and matrix[i+1][j]== 0:
    matrix[i+1][j]= 1
  if j-1>=0 and matrix[i][j-1]==0 :
    matrix[i][j-1]= 1
  if j+1<m and matrix[i][j+1] ==0:
    matrix[i][j+1]= 1

def zero(matrix):
  for i in matrix:
    if 0 in i:
      return False
  return True

matrix = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
breaked =False
while not zero(matrix):
  prev_matrix = copy.deepcopy(matrix)
  cnt+=1
  for i in range(n):
    for j in range(m):
      if matrix[i][j]==1:
        test(matrix, i, j)
  if prev_matrix== matrix:
    print(prev_matrix)
    print(matrix)
    breaked = True
    break
  for i in matrix:
    print(i)
  print('-------------------------------------------------')

if breaked:
  print(-1)
else: 
  print(cnt)