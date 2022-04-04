m, n = map(int, input().split())

Set = set(input() for _ in range(m))

cnt = 0
result = []

for _ in range(n):
    inp = input()
    if inp in Set:
        cnt += 1
        result.append(inp)

print(cnt)
result.sort()
for i in result:
    print(i)
