n = int(input())
arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    for j in i:
        print(j, end=" ")
    print()

