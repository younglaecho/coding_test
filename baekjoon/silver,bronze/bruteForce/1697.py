from collections import deque

start, to = map(int, input().split())
dist = [0]*100001

q = deque()
q.append(start)
while q:
    x = q.popleft()
    if x == to:
        print(dist[x])
        break
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= 100000 and not dist[nx]:
            dist[nx] = dist[x] + 1
            q.append(nx)
                
