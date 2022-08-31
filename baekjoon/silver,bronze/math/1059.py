n = int(input())

arr = list(map(int, input().split()))
arr.append(0)
arr.sort()
target = int(input())

for i in range(len(arr)):
    if target == arr[i]:
        print(0)
        break
    elif arr[i] > target:
        start = arr[i-1]
        end = arr[i]
        print((target-start-1)*(end-target)+end-target-1)
        break
