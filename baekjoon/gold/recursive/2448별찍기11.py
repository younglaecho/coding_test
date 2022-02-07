import time
n = int(input())

matrix = [[' ' for _ in range(2*n-1)] for _ in range(n)]
def show(matrix):
  for i in matrix:
    for j in i:
      # print(j, end='')
      pass
    print()

def star(x, y, n):
  if n == 3:
    matrix[x][y] = '*'
    matrix[x+1][y-1] = '*'
    matrix[x+1][y+1] = '*'
    for i in range(-2,3):
      matrix[x+2][y+i] = '*'
    return 
  ndiv = n//2
  star(x, y, ndiv)
  star(x+ndiv, y-ndiv, ndiv)
  star(x+ndiv, y+ndiv, ndiv)

star(0, n-1, n)


start = time.time()
show(matrix)
end = time.time()
print(end- start)


start = time.time()

for i in matrix:
  print("".join(i))

end = time.time()
print(end- start)
