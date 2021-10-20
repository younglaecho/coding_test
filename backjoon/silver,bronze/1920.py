n = int(input())

n_arr = list(map(int, input().split()))

m = int(input())

m_arr = list(map(int, input().split()))

set = set()

for i in n_arr:
  set.add(i)

for i in m_arr:
  if i in set:
    print(1)
  else:
    print(0)