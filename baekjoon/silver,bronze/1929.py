n, m = map(int, input().split())

def is_prime(number):
  if number == 1:
    return False
  else:
    for i in range(2, int(number**0.5)+1):
      if number%i==0:
        return False
    return True
for i in range(n, m+1):
  if is_prime(i):
    print(i)

