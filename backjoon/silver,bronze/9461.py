n = int(input())

arr = [1,1,1,2,2,3,4]+[0]*100
for i in range(7,101):
  arr[i]= arr[i-1]+arr[i-5]

for _ in range(n):
  num = int(input())
  print(arr[num-1])
