from collections import deque

m, n = map(int, input().split())

arr = list(map(int, input().split()))

queue = deque(range(1, m + 1))

cnt = 0
for number in arr:
    loc = queue.index(number)

    if len(queue) - loc > loc:
        queue.rotate(-loc)
        cnt += loc
    else:
        queue.rotate(len(queue) - loc)
        cnt += len(queue) - loc
    # print(cnt)
    queue.popleft()
print(cnt)
