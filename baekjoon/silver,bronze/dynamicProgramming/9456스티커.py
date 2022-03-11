test_case = int(input())

for _ in range(test_case):
    n = int(input())

    matrix = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(matrix[0][0], matrix[1][0]))
        continue

    matrix[0][1] += matrix[1][0]
    matrix[1][1] += matrix[0][0]

    for i in range(2, n):
        matrix[0][i] += max(matrix[1][i-2], matrix[1][i-1])
        matrix[1][i] += max(matrix[0][i-2], matrix[0][i-1])

    print(max(matrix[0][n-1], matrix[1][n-1]))
