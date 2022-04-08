n = input()
f = int(input())

n = int(n[:-2] + "00")

for i in range(100):
    number = n + i
    if number % f == 0:
        i = str(i)
        if len(i) == 1:
            print("0" + i)
        else:
            print(i)
        break
