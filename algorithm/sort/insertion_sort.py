def insert_sort(x):
    for i in range(1, len(x)):
        j = i - 1
        cur = x[i]
        while x[j] > cur and j >= 0:
            x[j+1] = x[j]
            j = j - 1
        x[j+1] = cur
    return x