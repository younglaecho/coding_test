def solution(routes):
    routes.sort(key=lambda x: x[1])
    cnt = 1
    pos = routes[0][1]

    for i in range(1, len(routes)):
        if pos < routes[i][0]:
            pos = routes[i][1]
            cnt += 1

    return cnt
