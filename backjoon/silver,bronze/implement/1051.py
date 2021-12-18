n, m = map(int, input().split())

matrix = [input() for _ in range(n)]
result = []
for i in range(10):
  for j in range(len(matrix)):
    if matrix[j].count(str(i)) > 1:
      start = matrix[j].find(str(i))
      last = matrix[j].rfind(str(i))
      gap = last-start
      if (j+gap)<n and matrix[j+gap][start]==str(i) and matrix[j+gap][last]==str(i):
        result.append((gap+1)**2)


if result:
  print(max(result))
else:
  print(1)