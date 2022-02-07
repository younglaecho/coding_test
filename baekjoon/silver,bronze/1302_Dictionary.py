n = int(input())
Dict = {}

for _ in range(n):
  value = input()
  if value in Dict:
    Dict[value] +=1
  else:
    Dict[value] = 1

arr = []
for k, v in Dict.items():
  if v == max(Dict.values()):
    arr.append(k)

print(sorted(arr)[0])