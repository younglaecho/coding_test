from heapq import heappush, heappop
import sys

input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    n = int(input())
    min_heap = []
    max_heap = []

    for _ in range(n):
        state, number = input().split()
        number = int(number)
        if state == "I":
            heappush(min_heap, number)
            heappush(max_heap, (-number, number))
        else:
            if max_heap:
                if number == 1:
                    Max = heappop(max_heap)
                    min_heap.remove(Max[1])
                else:
                    Min = heappop(min_heap)
                    max_heap.remove((-Min, Min))

    if max_heap == 0:
        print("EMPTY")
    else:
        print(heappop(max_heap)[1], heappop(min_heap))
