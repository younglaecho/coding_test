from collections import deque

gears = [deque(map(int, list(input()))) for _ in range(4)]

def show(matrix):
  for i in matrix:
    for j in i:
      print(j, end=' ')
    print()
# print()
# show(gears)
n = int(input())
for _ in range(n):
  number, direc = map(int, input().split())
  rotation = [0,0,0,0]
  rotation[number-1] = direc

  for i in range(number-2,-1,-1):
    if gears[i][2]!= gears[i+1][6]:
      rotation[i] = rotation[i+1]*(-1)
    else:
      break
  for j in range(number, 4):
    if gears[j][6]!= gears[j-1][2]:
      rotation[j] = rotation[j-1]*(-1)
    else:
      break
  for i in range(4):
    gears[i].rotate(rotation[i])


result = 0
n2 = 1
for gear in gears:
  result += gear[0]*n2
  n2*=2

print(result)