from collections import defaultdict
length = int(input())
arr = []

Dict = defaultdict(int)
total = 0
for _ in range(length):
  n = int(input())
  Dict[n] += 1
  arr.append(n)
  total+=n
arr.sort()
  
print(round(total/len(arr)))
print(arr[len(arr)//2])

max1 = sorted([k for k,v in Dict.items() if max(Dict.values()) == v])
if len(max1)>1:
  print(max1[1])
else:
  print(max1[0])

print(arr[-1]-arr[0])