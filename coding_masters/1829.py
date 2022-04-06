from collections import defaultdict

n = int(input())

Dict = defaultdict(int)

for i in range(1, n + 1):
    for j in str(i):
        Dict[j] += 1


for i in range(10):
    print(Dict[str(i)], end=" ")
