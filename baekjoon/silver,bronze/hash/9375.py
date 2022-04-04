from collections import defaultdict

n = int(input())
answer = []
for _ in range(n):
    m = int(input())

    Dict = defaultdict(int)
    for _ in range(m):
        a, b = input().split()
        Dict[b] += 1

    result = 1
    for cnt in Dict.values():
        result *= cnt + 1
    answer.append(result - 1)

for i in answer:
    print(i)
