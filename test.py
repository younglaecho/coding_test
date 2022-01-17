
from audioop import reverse


def solution(k, a, b):
  a.sort(reverse= True)
  b.sort(reverse= True)
  answer = 0
  for i in range(len(a)-k):
    answer += a[i]
  for i in range(k):
    if a[0]>b[0]:
      answer+=a.pop(0)
    else:
      answer+=b.pop(0)

  return answer

k = 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]
answer = solution(k, a, b)
print(answer)