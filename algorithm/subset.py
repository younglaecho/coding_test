from itertools import combinations 

arr = [1, 2, 3]
result = []
for i in range(len(arr)+1):
  result = result+list(combinations(arr,i))  

print(result)


subsets = [[]]

for num in arr:
  size = len(subsets)
  for y in range(size):
    subsets.append(subsets[y]+[num])
print(subsets)