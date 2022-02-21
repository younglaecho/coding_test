n = int(input())
mon = []
counts = []
for _ in range(n):
  mon.append(input())
  k, m = map(int, input().split())
  count = 0
  while k <= m:
    m = m-k+2
    count+=1
  counts.append(count)

print(sum(counts))
print(mon[counts.index(max(counts))])
