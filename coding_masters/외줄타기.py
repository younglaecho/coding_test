n, m = map(int, input().split())

Dict = {}
for _ in range(m):
    start, end, dist = map(int, input().split())
    Dict[start] = (end, dist)
    Dict[end] = (start, dist)

stack = []

while stack:
    