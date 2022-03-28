from math import factorial

n = int(input())

answer = str(factorial(n))[::-1]

cnt = 0
for i in answer:
    if i == "0":
        cnt += 1
    else:
        break

print(cnt)
