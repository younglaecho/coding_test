n = int(input())
arr = []
for i in range(n):
  input_data =list(map(int, input().split()))
  arr.append((input_data[0], input_data[1]))

arr.sort()

for i in arr:
  print(i[0],i[1])