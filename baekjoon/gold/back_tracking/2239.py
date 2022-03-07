import sys

imput = sys.stdin.readline
matrix = [list(map(int, list(input()))) for _ in range(9)]
empty = [(i, j) for i in range(9) for j in range(9) if matrix[i][j] == 0]


def check_hor(y, n):
    for i in range(9):
        if matrix[y][i] == n:
            return False
    return True


def check_ver(x, n):
    for i in range(9):
        if matrix[i][x] == n:
            return False
    return True


def check_box(x, y, n):
    a = (x // 3) * 3
    b = (y // 3) * 3

    for i in range(a, a + 3):
        for j in range(b, b + 3):
            if matrix[j][i] == n:
                return False
    return True


def DFS(depth):
    if depth == len(empty):
        for i in matrix:
            for j in i:
                print(j, end="")
            print()
        exit()

    ny, nx = empty[depth]
    for n in range(1, 10):
        if check_hor(ny, n) and check_ver(nx, n) and check_box(nx, ny, n):
            matrix[ny][nx] = n
            DFS(depth + 1)
            matrix[ny][nx] = 0


DFS(0)
