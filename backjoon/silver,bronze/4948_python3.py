n=123456*2
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

while True:
  number = int(input())
  if number == 0:
    break
  cnt = 0
  for i in primes:
    if number<i<=2*number:
      cnt += 1

  print(cnt)