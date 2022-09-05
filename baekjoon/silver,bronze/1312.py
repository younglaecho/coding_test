a, b, n = list(map(int, input().split()))

str1 = str(a/b)

# print(str1)
if (len(str1)>1+n):
    print(str1[1+n])
else:
    print(0)