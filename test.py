from math import factorial as fac


def solution(money, costs):
    coins = [1, 5, 10, 50, 100, 500]
    rates = []
    total_cost = 0
    for i in range(6):
        rates.append((costs[i]/coins[i], i))

    rates.sort(key=lambda x: (x[0], -x[1]))

    i = 0

    while money > 0:
        total_cost += (money // coins[rates[i][1]]) * costs[rates[i][1]]
        money %= coins[rates[i][1]]
        i += 1

    return total_cost


def solution(n, clockwise):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 1], [1, 1]]
    elif n == 3:
        return [[1, 2, 1], [2, 3, 2], [1, 2, 1]]

    if clockwise:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        start_point = [(0, 0), (n-1, 0), (n-1, n-1), (0, n-1)]
    else:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        start_point = [(0, 0), (0, n-1), (n-1, n-1), (n-1, 0)]

    for i in range(4):
        matrix[start_point[i][0]][start_point[i][1]] = 1
        x, y = start_point[i]  # i
        direct = i            # i
        line_number = 1
        line_count = 1

        for number in range(2, (n**2)//4+2 if (n**2) % 4 else (n**2)//4+1):
            x = x+dx[direct]
            y = y+dy[direct]
            matrix[y][x] = number

            line_number += 1
            if line_number == n-line_count:
                direct = (direct+1) % 4
                line_number = line_count
                line_count += 1

    return matrix


def solution(width, height, diagonals):
    total = 0
    for diagonal in diagonals:
        left_point = (diagonal[0]-1, diagonal[1])
        lower_point = (diagonal[0], diagonal[1]-1)

        left_left_side = fac(
            left_point[0]+left_point[1])/(fac(left_point[0])*fac(left_point[1])) % 10000019
        left_right_side = fac(width + height - lower_point[0]-lower_point[1])/(
            fac(width-lower_point[0])*fac(height-lower_point[1])) % 10000019
        left_total = (left_left_side * left_right_side) % 10000019

        right_left_side = fac(
            lower_point[0]+lower_point[1])/(fac(lower_point[0])*fac(lower_point[1])) % 10000019
        right_right_side = fac(width + height - left_point[0]-left_point[1])/(
            fac(width-left_point[0])*fac(height-left_point[1])) % 10000019
        right_total = (right_left_side * right_right_side) % 10000019

        total += (left_total + right_total) % 10000019
    return total % 10000019


def solution(n, edges):
    visited = [False] * n
    graph = [[n]*n for _ in range(n)]
    for edge in edges:
        a, b = edge
        graph[a-1][b-1] = graph[b-1][a-1] = 1

    for i in range(n):
        graph[i][i] = 0

    count = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    for k in range(n):
        for i in range(n):
            if i != k:
                for j in range(n):
                    if k != j and i != j:
                        if graph[i][j] == graph[i][k] + graph[k][j]:
                            print(i, k, j)
                            count += 1

    return count
