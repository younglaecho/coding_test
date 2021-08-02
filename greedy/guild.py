n = int(input())

data = list(map(int, input().split()))

data.sort()
count = 0
print(data)
while True:
    if data[-1] == len(data):
        count += 1
        break
    if data[-1] > len(data):
        break
    popped_data = data.pop()
    for i in range(popped_data-1):
        data.pop(0)
    count += 1

    print(data)

print(count)
