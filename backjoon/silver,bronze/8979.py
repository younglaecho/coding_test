n, k = map(int, input().split())
Dict = {}
for _ in range(n):
  i, gold, silver, bronze = map(int, input().split())
  Dict[i] ={'gold':gold, 'silver':silver, 'bronze': bronze}

# print(Dict)
cnt = 0 
for i in Dict:
  print(Dict[i]['gold'],  Dict[k]['gold'])

  if Dict[i]['gold'] > Dict[k]['gold']:
    cnt += 1
  elif Dict[i]['gold'] == Dict[k]['gold'] and Dict[i]['silver'] > Dict[k]['silver']:
    cnt += 1
  elif Dict[i]['gold'] == Dict[k]['gold'] and Dict[i]['silver'] == Dict[k]['silver'] and Dict[i]['bronze'] > Dict[k]['bronze']:
    cnt += 1

print(cnt+1)