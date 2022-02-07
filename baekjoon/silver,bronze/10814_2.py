n = int(input())
arr = []
for i in range(n):
  info = input().split()
  arr.append((int(info[0]), info[1]))

arr.sort(key=lambda x: x[0])

for i in arr:
  print(i[0],i[1])