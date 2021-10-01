N = int(input())

matrix = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * N for i in range(N)]
houses = []
house = 0

def search(i, j) :
  global house
  if i < 0 or j < 0 or i >= N or j>=N or matrix[i][j]==0:
    return
  matrix[i][j] = 0
  visited[i][j] = 1
  house += 1

  search(i+1, j)
  for ele in visited:
    print(ele)
  print('================================================')
  search(i-1, j)
  for ele in visited:
    print(ele)
  print('================================================')
  search(i, j+1)
  for ele in visited:
    print(ele)
  print('================================================')
  search(i, j-1)
  for ele in visited:
    print(ele)
  print('================================================')
  

for i in range(N):
  for j in range(N):
    if matrix[i][j] == 1 and visited[i][j] == 0:
      search(i, j)
      houses.append(house)
      house = 0

print(len(houses))
houses.sort()

for element in houses:
  print(element)


