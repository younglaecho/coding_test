n = int(input())
arr = []
for _ in range(n):
  arr.append(input())

arr.sort()

count_arr=[]
while len(arr) > 0:
  count = arr.count(arr[0])
  count_arr.append((arr[0], count))
  for _ in range(count):
    del arr[0]

print(count_arr[count_arr.index(max(count_arr, key=lambda x:x[1]))][0])