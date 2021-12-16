# n = int(input())
# A = list(map(int, input().split()))
# answer = [-1] * n
# stack = []


# stack.append(0)
# for i in range(1, n):
#     while stack and A[stack[-1]] < A[i]:
#         answer[stack.pop()] = A[i]
#     stack.append(i)


# print(*answer)

n = int(input())
A = list(map(int, input().split()))
result = []
for i in range(0, n):
  for j in range(i+1,n):
    if A[j]>A[i]:
      result.append(A[j])
      break
  else:
    result.append(-1)

for ele in result:
  print(ele, end=" ")