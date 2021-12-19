n, m = map(int, input().split())

matrix = [input() for _ in range(n)]
result = []
for i in range(10):
  for j in range(len(matrix)):
    if matrix[j].count(str(i)) > 1:
      start = matrix[j].find(str(i))
      last = matrix[j].rfind(str(i))
      gap = last-start
      # print(start, last,gap)
      if (j+gap)<n and int(matrix[j+gap][start])==i and int(matrix[j+gap][last])==i:
        result.append((gap+1)**2)
      if (j-gap)>=0 and int(matrix[j-gap][start])==i and int(matrix[j-gap][last])==i:
        result.append((gap+1)**2)
      # print(i,j,start,last)
      # print(j, result)
if result:
  print(max(result))
else:
  print(1)