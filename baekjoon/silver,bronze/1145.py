from itertools import combinations
from math import lcm

data = list(map(int, input().split()))

three_data = list(combinations(data, 3))

answer = 0
for three in three_data:
    if answer > lcm(three[0], three[1], three[2]) or answer == 0:
        answer = lcm(three[0], three[1], three[2])

print(answer)
