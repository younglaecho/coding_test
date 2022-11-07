import sys
input = sys.stdin.readline
n, m = map(int, input().split())

matrix = [[0 for _ in range(m)]for _ in range(n)]

arr = list(map(int, input().split()))
i = 0
for a in arr:
    for j in range(a):
        matrix[j][i] = 1
    i+=1

flag_arr = [bool(i[0]) for i in matrix]

tot = 0
for i in range(n):
    num = 0
    flag = flag_arr[i]
    for j in range(m):
        if matrix[i][j] == 1:
            if flag:
                tot += num
            flag = True
            num = 0
            continue
        num += 1

print(tot)