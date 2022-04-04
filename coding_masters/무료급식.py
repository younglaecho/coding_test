from heapq import heappop, heappush

n = int(input())

heap = []
tmp = []

for i in range(n):
    age, name = input().split()
    heappush(heap, (-int(age), i))
    tmp.append(name)

for _ in range(n):
    age, number = heappop(heap)
    print(tmp[number])
