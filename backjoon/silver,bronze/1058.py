n = int(input())
arr = []
for i in range(n):
  arr.append(input())

result = []
for i in range(n):
  Set = set()
  for j in range(len(arr[i])):
    if arr[i][j] =='Y':
      Set.add(j)
      for k in range(len(arr[j])):
        if arr[j][k] == 'Y' and i !=k:
          Set.add(k)
  result.append(len(Set))
print(max(result))