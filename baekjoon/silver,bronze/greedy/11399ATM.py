n = int(input())

arr = list(map(int, input().split()))

arr.sort()

answer = arr[0]
for i in range(1, len(arr)):
    answer += arr[i-1] + arr[i]
    arr[i] += arr[i-1]
    
print(answer)