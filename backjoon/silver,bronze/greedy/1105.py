l, r = input().split()

cnt= 0
if len(l) == len(r):
  for i in range(len(l)):
    if l[i]==r[i]:
      if l[i]=='8':
        cnt+=1
    else:
      break

print(cnt)