a, b= map(int, input().split())
results = []
def recur(n, cnt):
  if n>b:
    return

  if n==b:
    results.append((n,cnt)) 
    return
    
  recur(n*2, cnt+1)
  recur(int(str(n)+'1'), cnt+1)

recur(a, 0)
if results:
  print(min(results, key=lambda x:x[1])[1]+1)
else:
  print(-1)