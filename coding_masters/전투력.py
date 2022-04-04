n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
result = []

for _ in range(n):
    length = len(arr)
    Min = arr.pop()
    result.append(Min * length)

print(max(result))
