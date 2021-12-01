n, c = list(map(int, input().split()))

array = []
for _ in range(n):
  array.append(int(input()))
array = sorted(array)

start = 1
end = array[-1]-array[0]
result = 0
while (start<=end):
  cnt = 1
  gap = (end+start)//2
  value = array[0]
  for i in range(1, len(array)):
    if array[i]>=value+gap:
      cnt+=1
      value= array[i]
  if cnt >= c:
    start = gap+1
    result = gap
  else:
    end = gap-1

print(result)