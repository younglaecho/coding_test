matrix = [list(map(int, list(input()))) for _ in range(9)]

hor_check = [[False for _ in range(10)] for _ in range(9)]
ver_check = [[False for _ in range(10)] for _ in range(9)]
box_check = [[False for _ in range(10)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        if matrix[i][j]:
            hor_check[i][matrix[i][j]] = True
            ver_check[j][matrix[i][j]] = True
            box_check[((i // 3) * 3) + (j // 3)][matrix[i][j]] = True


def dfs(n):
    if n == 81:
        for i in matrix:
            for j in i:
                print(j, end="")
            print()
        return True

    x = n % 9
    y = n // 9

    if matrix[y][x] != 0:
        return dfs(n + 1)
    else:
        for i in range(1, 10):
            if (
                not hor_check[y][i]
                and not ver_check[x][i]
                and not box_check[((y // 3) * 3) + (x // 3)][i]
            ):
                hor_check[y][i] = True
                ver_check[x][i] = True
                box_check[((y // 3) * 3) + (x // 3)][i] = True
                matrix[y][x] = i
                if dfs(n + 1):
                    return True
                hor_check[y][i] = False
                ver_check[x][i] = False
                box_check[((y // 3) * 3) + (x // 3)][i] = False
                matrix[y][x] = 0


dfs(0)
