n = int(input())
arr = [input() for i in range()]

arr.sort(key=lambda x: (len(x), x))

for i in arr:
    print(i)
