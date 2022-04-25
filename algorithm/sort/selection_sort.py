def selectionSort(x):
    length = len(x)
    for i in range(length-1):
        minidx = i
        for j in range(i+1, length):
            if x[minidx] > x[j]:
                minidx = j
        x[i], x[minidx] = x[minidx], x[i]
    return x