c = int(input())

network = {}
for _ in range(c):
  name1, name2 = input().split()
  
  network[name1]=name2
  network[name2]=name1