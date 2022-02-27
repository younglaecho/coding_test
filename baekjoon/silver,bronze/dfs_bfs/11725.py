import sys
sys.setrecursionlimit(10000000)
from collections import defaultdict

n = int(input())

graph = defaultdict(list)
visited = [False]*(n+1)
result = [0]*(n+1)
for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


def dfs(graph, i, visited):
  visited[i] = True
  
  for j in graph[i]:
    if not visited[j]:
      dfs(graph, j, visited)
      result[j] = i

dfs(graph, 1, visited)


for i in range(2, n+1):
  print(result[i])