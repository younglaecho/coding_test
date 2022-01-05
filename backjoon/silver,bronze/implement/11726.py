arr = [1,2,3,5,8]+[0]*1000
n = int(input())

for i in range(4, n+1):
  arr[i] = arr[i-2] + arr[i-1]

print(arr[n-1]%10007)