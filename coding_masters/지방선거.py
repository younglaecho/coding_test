from collections import defaultdict

n = int(input())
Dict = defaultdict(int)

for _ in range(n):
    Dict[int(input())] += 1

result = [k for k, v in Dict.items() if max(Dict.values()) == v]

result.sort()
print(result[0])
