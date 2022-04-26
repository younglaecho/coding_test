def bubbleSort(x):
    length = len(x) - 1
    for i in range(length):
        for j in range(length - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


arr = [21, 10, 10, 12, 20, 25, 26, 25, 13, 15, 22]

print(bubbleSort(arr))
