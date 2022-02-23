n = int(input())

arr = list(map(int,input().split()))
result = []

if n<3:
  print(max(arr))
else:
  result.append(arr[0])

  for i in range(1, n-1):
    result.append(arr[i]+ min(arr[i-1], arr[i+1]))
  result.append(arr[-1])
  print(max(result))