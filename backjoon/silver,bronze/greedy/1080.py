n, m = map(int, input().split())

prev_matrix = [list(map(int, input())) for _ in range(n)]
result_matrix = [list(map(int, input())) for _ in range(n)]

count = 0
for i in range(n-2):
  for j in range(m-2):
    if prev_matrix[i][j] != result_matrix[i][j]:
      for a in range(3):
        for b in range(3):
          prev_matrix[i+a][j+b] = 1-prev_matrix[i+a][j+b]
      count+=1

breaked = False
for i in range(n):
  for j in range(m):
    if prev_matrix[i][j] != result_matrix[i][j]:
      breaked = True
      break
# if n<3 or m<3:
#   breaked = True
if breaked:
  print(-1)
else:
  print(count)