n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = []
stack.append(1)
result = []
while stack:
    x = stack.pop()

    if not visited[x]:
        graph[x].sort(reverse=True)
        stack.extend(graph[x])
        visited[x] = True
        result.append(x)

for ele in result:
    print(ele, end=" ")
