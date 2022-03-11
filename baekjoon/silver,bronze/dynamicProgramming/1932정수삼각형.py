n = int(input())

tri = [list(map(int, input().split())) for _ in range(n)]

cnt = 1
for i in range(1, n):
    cnt +=1
    for j in range(cnt):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == cnt-1:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

print(max(tri[n-1]))