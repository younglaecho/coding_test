import sys

n = int(sys.stdin.readline())
aparts = [list(map(int,sys.stdin.readline()[0:-1])) for _ in range(int(n))]

cnt = 2
buildings = {}

def showBuildings(matrix):

  for col in matrix:
    print(col)

  print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')

def makeBuildings(i, j, cnt):

  if aparts[i][j] != cnt:
    aparts[i][j] = cnt
    buildings[cnt] += 1
  
  if i > 0 and aparts[i-1][j]==1:
    aparts[i-1][j]=cnt
    buildings[cnt] += 1
    makeBuildings(i-1, j, cnt)

  if j > 0 and aparts[i][j-1]==1:
    aparts[i][j-1]=cnt
    buildings[cnt] += 1
    makeBuildings(i, j-1, cnt)

  if i < n-1 and aparts[i+1][j]==1:
    aparts[i+1][j]=cnt
    buildings[cnt] += 1
    makeBuildings(i+1, j, cnt)

  if j < n-1 and aparts[i][j+1]==1:
    aparts[i][j+1]=cnt
    buildings[cnt] += 1
    makeBuildings(i, j+1, cnt)

for i in range(n):
  for j in range(n):
    if aparts[i][j]==1:
      buildings[cnt] = 0
      makeBuildings(i, j, cnt)
      showBuildings(aparts)
      cnt += 1

print(buildings)