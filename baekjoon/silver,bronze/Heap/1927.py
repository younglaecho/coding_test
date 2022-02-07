import heapq


heap = []
result = []
test_case = int(input())

for _ in range(test_case):
  n = int(input())
  if n ==0:
    if heap:
      result.append(heapq.heappop(heap))
    else:
      result.append(0)
  else:
    heapq.heappush(heap, n)
  
for i in result:
  print(i)


# 코드 중간에 print를 하는 것보다 result에 담은 후에 배열을 순회하면서 출력하는 것이 더 빠름.. 