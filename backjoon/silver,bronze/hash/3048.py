m, n = map(int, input().split())

forward = list(input())
backward = list(input())

times = int(input())
forward.reverse()
directions = {}

for element in forward:
  directions[element] = 1

for element in backward:
  directions[element] = 0

position = forward + backward


for _ in range(times):
  i = 0
  while True:
    if directions[position[i]] and not  directions[position[i+1]]:
      tmp = position[i]
      position[i] = position[i+1]
      position[i+1] = tmp
      i += 1
    i += 1
    if i >=len(position) -1:
      break


print(''.join(position))