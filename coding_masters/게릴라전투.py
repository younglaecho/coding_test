a = int(input())

arr = [int(input()) for _ in range(a)]

b, c = map(int, input().split())

cnt = 0
for ele in arr:
    cnt += 1
    ele -= b
    if ele > 0:
        if ele // c == ele / c:
            cnt += ele // c
        else:
            cnt += ele // c + 1

print(cnt)
