n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())

    arr.append((a, b))

arr.sort()

cnt = 0
end = 0

for a, b in arr:
    if end > b:
        end = b
    elif a >= end:
        end = b
        cnt += 1

print(cnt)
