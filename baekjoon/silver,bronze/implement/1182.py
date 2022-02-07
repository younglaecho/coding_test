n, answer = map(int, input().split())

arr = list(map(int, input().split()))

subsets = [[]]

for num in arr:
  size = len(subsets)
  for y in range(size):
    subsets.append(subsets[y]+[num])

cnt = 0
subsets.pop(0)
for subset in subsets:
  if sum(subset) == answer:
    cnt+=1
print(cnt)