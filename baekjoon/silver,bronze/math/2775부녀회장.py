test_case = int(input())
matrix = [[i for i in range(15)]]
matrix += [[0 for _ in range(15)] for _ in range(14)]

for i in range(1, 14):
    for j in range(1, 15):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

# show(matrix)
for _ in range(test_case):
    k = int(input())
    n = int(input())

    print(matrix[k][n])
