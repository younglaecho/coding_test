number, total = map(int, input().split())

coins = [int(input()) for _ in range(number)]
coins.reverse()
cnt = 0
for i in range(number):
  if total == 0:
    break
  if coins[i]> total:
    continue
  cnt += total // coins[i]
  total = total % coins[i]


print(cnt)
