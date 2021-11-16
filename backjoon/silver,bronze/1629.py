def power(a, b, c) :
  if b==1:
    return a % c
  else:
    temp = power(a, b//2,c)
    if b%2 ==1:
      return (temp*temp*a) %c
    else:
      return (temp*temp) % c

a, b, c = map(int, input().split())
print(power(a,b,c))
