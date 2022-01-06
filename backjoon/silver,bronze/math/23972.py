import math
k,n=map(int,input().split())

if n == 1:
  print(-1)
else:
  if math.ceil(k*n/(n-1))>k:
    print(math.ceil(k*n/(n-1)))
  else:
    print(-1)