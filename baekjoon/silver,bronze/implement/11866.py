n, k = map(int, input().split())

arr = []
for i in range(1, n+1):
    arr.append(i)
# [1, 2, 3, 4, 5, 6, 7]

cnt = -1
result = []

while arr:
    cnt+=k
    cnt%=len(arr)
    result.append(arr.pop(cnt))
    cnt-=1

print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(str(result[-1])+'>')



# from collections import deque

# arr = deque()
# for i in range(1, n+1):
#     arr.append(i)

# result = []
# while arr:
#     arr.rotate(-2)
#     result.append(arr.popleft())

# print('<', end='')
# for i in range(len(result)-1):
#     print(result[i], end=', ')
# print(str(result[-1])+'>')