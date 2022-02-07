test_case = int(input())

for _ in range(test_case):
  a, b = map(int, input().split())
  period = []
  if b == 1:
    print(a%10 if a%10 else 10)
    continue
  for i in range(1, b+1):
    if (a**i)%10 in period:
      break
    period.append((a**i)%10)

  if len(period)<=b:
    print(period[b%len(period)-1] if period[b%len(period)-1] else 10)
  else: 
    print(period[-1])