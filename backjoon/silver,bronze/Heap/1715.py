import heapq

n = int(input())

heap = []

for _ in range(n):
  heap.append(int((input())))
heap.sort()
for i in range(1,len(heap)):
  heap[i] = heap[i]+heap[i-1]
print(sum(heap[1:]))
