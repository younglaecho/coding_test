m, n = map(int, input().split())
matrix = [input() for _ in range(m)]
result = 32
# print(matrix)
def change(x, y):
  B_init = 0
  W_init = 0
  for i in range(8):
    for j in range(8):
      if (i+j)%2 == 1 and matrix[x+i][y+j] == 'W':
        W_init+=1
      if (i+j)%2 == 0 and matrix[x+i][y+j] == 'B':
        W_init+=1

      if (i+j)%2 == 1 and matrix[x+i][y+j] == 'B':
        B_init+=1
      if (i+j)%2 == 0 and matrix[x+i][y+j] == 'W':
        B_init+=1  
  return min(W_init, B_init)


for i in range(m-7):
  for j in range(n-7):
    result = min(result,change(i, j))

print(result)

# change(0, 5)