for _ in range(int(input())):
  n, m = map(int, input().split())
  queue = list(map(int, input().split()))
  orders = [i for i in range(n)]
  cnt = 0
  while len(queue):
    if queue[0] == max(queue):
      cnt += 1
      check = queue.pop(0)
      order = orders.pop(0)
      if order == m:
        print(cnt)
        break
    else:
      queue.append(queue.pop(0))
      orders.append(orders.pop(0))
