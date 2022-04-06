total, n = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

cnt = 0
while arr:
    if total < 0:
        break
    if arr[-1] <= total:
        tmp = arr.pop()
        total -= tmp
        cnt += 1
    else:
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] <= total:
                cnt += 1
                break
        break


print(cnt)
