n = int(input())

cnt = 0
init = 1
while n!=0:
  if n-init>=0:
    n = n-init
    init+=1
    cnt+=1
  else:
    init = 1

print(cnt)
