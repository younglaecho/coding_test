a, b, n = map(int, input().split())

str1 = list()

for _ in range(n):
    a = (a - (a // b)*b)*10
    str1.append(a // b)

print(str1[n-1])