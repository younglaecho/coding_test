from itertools import combinations
n = int(input())

data = list(map(int, input().split()))

comb = set()
for i in range(1, len(data)+1):
    comb = comb | (set(combinations(data, i)))

a = []
for list in comb:
    a.append(sum(list))
a.sort()
print(a)
numbers = [i for i in range(1, 1000001)]

for number in numbers:
    if not number in a:
        print(number)
        break
