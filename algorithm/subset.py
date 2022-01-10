# itertools
from itertools import combinations 

arr = [1, 2, 3]
result = []
for i in range(len(arr)+1):
  result = result+list(combinations(arr,i))  

print(result)


# for 
subsets = [[]]

for num in arr:
  size = len(subsets)
  for y in range(size):
    subsets.append(subsets[y]+[num])
print(subsets)


#recursion
import copy
result = []
def recur(subset, i, arr):
  if i == len(arr):
    result.append(copy.copy(subset))
    return 
  else:
    subset.append(arr[i])
    i += 1
    recur(subset, i, arr)
    subset.pop()
    recur(subset, i, arr)
    

recur([], 0, arr)
print(result)


# 비트연산
arr = [1,2,3] 
result = []
for i in range(1<<len(arr)): # 공집합을 제외한 모든 부분집합 검사 
  subset = []
  for j in range(len(arr)): # arr의 모든 원소 루프
    if i & (1<<j): # i의 j번째 비트 검사, j번째 비트가 1이라면 arr[j] 출력
      subset.append(arr[j]) # 출력하면 순서가 바뀜에 유의, 다시 말해서 0번째 비트를 검사하면 3의 위치를 검사하는데 arr[j]는 arr[0]을 말한다. 고로 1이 출력됨.
  result.append(subset)
print(result)