for _ in range(int(input())):
  n, m = list(map(int, input().split()))
  queue = list(map(int, input().split()))
  orders = [i for i in range(n)]
  cnt = 0
  while len(queue):
    if queue[0] == max(queue):
      check = queue.pop(0)
      order = orders.pop(0)
      cnt += 1
      if order == m:
        print(cnt)
        break
    else:
      temp = queue[0]
      queue.pop(0)
      queue.append(temp)
      temp = orders[0]
      orders.pop(0)
      orders.append(temp)
    print(queue)
    print(orders)