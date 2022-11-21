from heapq import heappop, heappush
from itertools import combinations
import copy

n, m, d = map(int, input().split());
matrix = [list(map(int, input().split())) for _ in range(n)]
arr = []

castle = [i for i in range(m)]
archer_cases = list(combinations(castle, 3))

def getEnemyNum():
    global arr
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt+=1
    
    return cnt


def killEnemy(archer_position):
    global arr
    remove_list = []
    attacked = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0

    for archer_pos in archer_position:
        pq = []

        for i in range(n-1, -1, -1):
            for j in range(m):
                if arr[i][j] == 1:
                    diff = abs(n-i) + abs(archer_pos-j)
                    if diff <= d:
                        heappush(pq, [diff, j, i])
        
        if pq:
            _, x, y = heappop(pq)
            remove_list.append([y, x])
    
    for y, x in remove_list:
        if not attacked[y][x]:
            attacked[y][x] = True
            cnt +=1
            arr[y][x] = 0

    return cnt


def moveEnemy():
    global arr
    arr[-1] = [0 for _ in range(m)]

    for i in range(-1, -n, -1):
        arr[i] = arr[i-1]

    arr[0] = [0 for _ in range(m)]


def game(archer_position):
    global arr
    cnt = 0

    while getEnemyNum() != 0:
        cnt += killEnemy(archer_position)
        moveEnemy()
    return cnt

answer = 0

for archer_position in archer_cases:
    arr = copy.deepcopy(matrix)
    cnt = game(archer_position)
    if answer < cnt:
        answer = cnt
        
print(answer)