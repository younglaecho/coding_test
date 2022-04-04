from collections import deque

target, n = map(int, input().split())

dp = []

result = []

min_depth = 100000


def recur(n, depth):
    global min_depth

    if min_depth < depth:
        return

    if target == n:
        min_depth = min(min_depth, depth)
        return

    if target < n:
        recur(n - 1, depth + 1)

    else:
        recur(n * 2, depth + 1)
        recur(n + 1, depth + 1)


recur(n, 0)
print(result)

# queue = deque()
# queue.append((n, 0))
# min_depth = 1000000

# while queue:
#     n, depth = queue.popleft()
#     print(n)
#     if n > target:
#         queue.append((n - 1, depth + 1))

#     if n == target:
#         result.append(depth)
#         break
#     else:
#         if min_depth > depth:
#             queue.append((n * 2, depth + 1))
#             queue.append((n + 1, depth + 1))

# print(min(result))
