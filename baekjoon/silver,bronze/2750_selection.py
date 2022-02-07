n = int(input())
result = []
for _ in range(n):
  number = int(input())
  result.append(number)

for i in range(n):
  min_index = i
  for j in range(i+1,n):
    if result[j]<result[min_index]:
      min_index=j
  result[i],result[min_index] = result[min_index], result[i]
for i in result:
  print(i)