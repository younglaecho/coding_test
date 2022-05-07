n, m = map(int, input().split())

cp = []
for _ in range(n):
    p, v = map(int, input().split())
    if cp:
        cp.append((p+cp[-1][0], v))
    else:
        cp.append((p, v))

List = []
for _ in range(m):
    d, v = map(int, input().split())
    if List:
        List.append((d+List[-1][0], v))
    else:
        List.append((d, v))

prev = 0

def find_between(prev, cur):
    for p, v in cp:
        if prev < p < cur:
            return p, v
    return False

def find_upper(cur):
    for p, v in cp:
        if p>=cur:
            return p, v

Max = 0

for i in range(m):
    cur = List[i][0]
    if find_between(prev, cur):
        Max = max(List[i][1]-find_between(prev, cur)[1], Max)
    Max = max(List[i][1]-find_upper(cur)[1], Max)
    prev = cur

print(Max)