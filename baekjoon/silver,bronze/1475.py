string = input()
Dict = {}
for i in range(1,10):
  Dict[str(i)] = 0
for i in string:
  if i in Dict.keys():
    Dict[i] += 1
  else:
    Dict[i] = 1

if '6' in Dict.keys() or '9' in Dict.keys():
  Dict['6'] = (Dict['6']+Dict['9'])//2 +(Dict['6']+Dict['9'])%2 
  del Dict['9']

print(max(Dict.values()))