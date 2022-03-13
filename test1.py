# import sys
# from collections import deque

# # sys.stdin = open('input.txt', 'r')

# n,m = map(int, input().split())
# graph = [list(map(int, input().strip())) for _ in range(n)]

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(x,y):
#   count = 0
#   queue = deque()
#   queue.append((x,y))
#   while queue:
#     x, y = queue.popleft()
#     for i in range(4):
#       nx = x+dx[i]
#       ny = y+dy[i]
#       if nx<0 or ny<0 or nx>=n or ny>=m:
#         continue
#       if graph[nx][ny] == 0:
#         continue
#       if graph[nx][ny] == 1:
#         graph[nx][ny] = graph[x][y]+1
#         queue.append((nx,ny))
#   return graph[n-1][m-1], graph

# print(bfs(0,0))


from math import factorial as fac

n, m = map(int, input().split())

print(fac(n)//(fac(m)*fac(n-m)))
