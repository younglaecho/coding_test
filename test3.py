import time


def func1(arr):
    start = time.time()
    for i in range(len(arr)):
        if i < int(len(arr) / 3):
            arr[i] += i
        elif i < int(len(arr) * 2 / 3):
            arr[i] += i
        else:
            arr[i] += i
    end = time.time()
    print(end - start)


def func2(arr1, arr2, arr3):
    start = time.time()

    for i in range(len(arr1)):
        if i < int(len(arr1) / 3):
            arr1[i] += i
        elif i < int(len(arr1) * 2 / 3):
            arr2[i] += i
        else:
            arr3[i] += i

    end = time.time()
    print(end - start)


n = 1000000

bigarr = list(range(n * 3))
arr1 = list(range(n * 3))
arr2 = list(range(n * 3))
arr3 = list(range(n * 3))


func1(bigarr)
func2(arr1, arr2, arr3)
