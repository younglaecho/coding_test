# import heapq

# heap = []
# result = []
# test_case = int(input())

# for _ in range(test_case):
#   n = int(input())

#   if n == 0:
#     if heap:
#       print(heapq.heappop(heap))
#     else:
#       print(0)
#   else:
#     heapq.heappush(heap, n)

# for i in result:
#   print(i)

import heapq

heap = []
result = []
test_case = int(input())

for _ in range(test_case):
  n = int(input())

  if n == 0:
    if heap:
      result.append(heapq.heappop(heap))
    else:
      result.append(0)
  else:
    heapq.heappush(heap, n)

for i in result:
  print(i)