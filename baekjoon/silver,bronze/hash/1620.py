import sys

input = sys.stdin.readline
n, m = map(int, input().split())
Dict = dict()
List = [0]
cnt = 0

for _ in range(n):
    cnt += 1
    v = input()
    List.append(v)
    Dict[v] = cnt

for _ in range(m):
    v = input()
    try:
        List[int(v)]
        print(List[int(v)])
    except:
        print(Dict[v])
