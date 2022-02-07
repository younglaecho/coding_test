n = int(input())
arr = []
for i in range(n):
  info = input().split()
  info[0] = int(info[0])
  arr.append(tuple(info))

arr.sort(key=lambda x: x[0])

for i in range(n):
  print(arr[i][0],arr[i][1])