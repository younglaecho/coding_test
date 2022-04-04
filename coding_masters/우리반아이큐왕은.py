from heapq import heappush, heappop

n = int(input())
heap = []
List = []

for i in range(n):
    name, score = input().split()
    List.append(name)
    heappush(heap, (-int(score), i))

for _ in range(3):
    print(List[heappop(heap)[1]])
