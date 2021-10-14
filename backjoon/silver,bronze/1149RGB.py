n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
  matrix[i][0] = matrix[i][0]+ min(matrix[i-1][1], matrix[i-1][2])
  matrix[i][1] = matrix[i][1]+ min(matrix[i-1][0], matrix[i-1][2])
  matrix[i][2] = matrix[i][2]+ min(matrix[i-1][0], matrix[i-1][1])

print(min(matrix[n-1]))