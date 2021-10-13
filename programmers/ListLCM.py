from math import gcd
def LCM(x, y):
    return x*y/gcd(int(x), int(y))


def solution(arr):
    lcm = 1
    for i in range(len(arr)):
        lcm = LCM(lcm,arr[i])
    return lcm