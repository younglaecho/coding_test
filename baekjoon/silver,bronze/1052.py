n, k = map(int, input().split())

def test(num):
  result = 0
  while True:
    a = num//2
    b = num%2
    result += b
    num = a
    if num == 0:
      break
  return result

i = n
while True:
  if test(i) <=k:
    print(i-n)
    break
  else:
    i+=1