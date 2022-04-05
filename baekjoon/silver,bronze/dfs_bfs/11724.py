from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
n, m = map(int, input().split())
Dict = defaultdict(list)
visited = [False]*(n+1)

for _ in range(m):
    start, end = map(int, input().split())
    Dict[start].append(end)
    Dict[end].append(start)

def dfs(graph, i, visited):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, j, visited)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(Dict, i, visited)
        cnt+=1

print(cnt)

    