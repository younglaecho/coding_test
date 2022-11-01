n, m = map(int, input().split())

matrix = [[0 for _ in range(m)]for _ in range(n)]

# def show_matrix(mat):
#     for arr in mat:
#         print(arr)

arr = list(map(int, input().split()))
i = 0
for a in arr:
    for j in range(a):
        matrix[j][i] = 1
    i+=1
# show_matrix(matrix)

tot = 0
for i in range(n):
    num = 0
    flag = True
    for j in range(m):
        if matrix[i][j] == 1:
            if flag:
                tot += num
                num = 0
                continue
            else :
                num = 0
                flag = True
                continue

        num += 1
        if j == 0 and matrix[i][j] == 0:
            flag = False

print(tot)