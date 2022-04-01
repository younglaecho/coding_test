from curses.ascii import isdigit
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
Dict = dict()
List = [0]
cnt = 0

for _ in range(n):
    cnt += 1
    v = input().strip()
    List.append(v)
    Dict[v] = cnt

for _ in range(m):
    v = input().strip()
    if v.isdigit():
        print(List[int(v)])
    else:
        print(Dict[v])
