n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = 0

while True:
  max_val = max(arr)
  max_index = arr.index(max_val)
  if max_index==0:
    break
  arr[0]+=1
  arr[max_index]-=1
  cnt+=1

if arr.count(max_val)==1:
  print(cnt)
else:
  print(cnt+1)