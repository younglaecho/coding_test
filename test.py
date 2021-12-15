n = int(input())

for _ in range(n):
  m, n =input().split()
  answer = ''
  for i in n:
    answer += i*int(m)
  print(answer)