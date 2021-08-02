from itertools import combinations

n, m = list(map(int, input().split()))

data = list(map(int, input().split()))

combs = list(combinations(data, 2))

count = 0
for comb in combs:
    if comb[0] != comb[1]:
        count += 1

print(count)
