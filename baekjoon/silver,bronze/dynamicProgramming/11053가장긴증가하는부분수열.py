n = int(input())

arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
dp2 = [[] for _ in range(n)]
dp2[0].append(arr[0])
# print(dp2)

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[i] >= dp[j] + 1:
                pass
            else:
                dp[i] = dp[j] + 1
                dp2[i] = list(dp2[j]) + [arr[i]]
    if not dp2[i]:
        dp2[i] = [arr[i]]

print(max(dp))

for i in dp2[dp.index(max(dp))]:
    print(i, end=" ")
