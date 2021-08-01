N, M, K = map(int, input().split())
data = list(map(int, input().split()))


data.sort()

bigNum = data[-1]
subBignum = data[-2]

count = 0
result = 0
for i in range(M):
    if count == K:
        result += subBignum
        count = 0
    else:
        result += bigNum
        count += 1

print(result)
