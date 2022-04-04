m, n = map(int, input().split())

Dict = {}
for _ in range(m):
    left, right = input().split()
    Dict[left] = right

for _ in range(n):
    print(Dict[input()])
