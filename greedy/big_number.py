N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

bigNum = data[-1]
subBignum = data[-2]

result = (M // (K+1)) * (K * bigNum + subBignum) + (M % (K+1)) * bigNum

print(result)
