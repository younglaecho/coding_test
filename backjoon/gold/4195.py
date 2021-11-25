n = int(input())

def find(name):
  if name==parent[name]:
    return name
  else:
    p = find(parent[name])
    parent[name] = p
    return parent[name]

def union(name1, name2):
  name1 = find(name1)
  name2 = find(name2)

  if name1 != name2:
    parent[name2] = name1
    numbers[name1] += numbers[name2]

for _ in range(n):
  parent = dict()
  numbers = dict()

  number = int(input())
  for _ in range(number):
    name1, name2 = input().split()

    if name1 not in parent:
      parent[name1] = name1
      numbers[name1] = 1

    if name2 not in parent:
      parent[name2] = name2
      numbers[name2] = 1
    
    union(name1, name2)
    print(numbers[find(name1)])
  print(numbers[find('f')], end=' ')
  print(numbers[find('ba')], end=' ')
  print(numbers[find('be')], end=' ')
  print(numbers[find('w')])
  print(parent[find('f')], end=' ')
  print(parent[find('ba')], end=' ')
  print(parent[find('be')], end=' ')
  print(parent[find('w')], end=' ')
