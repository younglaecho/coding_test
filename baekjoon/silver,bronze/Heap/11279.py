from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())
heap = []

result = []
for _ in range(n):
    state = int(input().strip())
    if state == 0:
        if heap:
            result.append(heappop(heap))
        else:
            result.append(0)
    else:
        heappush(heap, (-state))


for ele in result:
    print(-ele)
    