from collections import defaultdict
import heapq

n, m = map(int, input().split())
k = int(input())
INF = 1e8

graph = defaultdict(list)
dist = [INF] * (n + 1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # (거리, 대상)


def dijkstra(start):
    queue = [(0, start)]
    dist[start] = 0

    while queue:
        d, cur_node = heapq.heappop(queue)

        if dist[cur_node] < d:
            continue

        for i in graph[cur_node]:
            if d + i[0] < dist[i[1]]:
                dist[i[1]] = d + i[0]
                heapq.heappush(queue, (d + i[0], i[1]))


dijkstra(k)

for i in range(1, n + 1):
    print("INF" if dist[i] == INF else dist[i])
