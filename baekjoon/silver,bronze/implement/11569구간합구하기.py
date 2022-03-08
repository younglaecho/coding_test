import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = list(map(int, input().split()))

input_list = []
Max = 0

for _ in range(m):
    a, b = map(int, input().split())
    Max = max(Max, b)
    input_list.append((a, b))

for i in range(1, Max):
    arr[i] += arr[i - 1]

for x, y in input_list:
    print(arr[y - 1] - arr[x - 2])
