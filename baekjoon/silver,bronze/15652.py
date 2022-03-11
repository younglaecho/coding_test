import sys
sys.setrecursionlimit(10**9)
n, m = map(int, input().split())

arr = [i for i in range(1, n)]
result = []
def sol(a, List):
    if len(List) == m:
        result.append(list(List))
        return
    for i in range(a, n+1):
        List.append(i)
        sol(i, List)
        List.pop()

sol(1, [])

for i in result:
    for j in i:
        print(j, end=' ')
    print()
