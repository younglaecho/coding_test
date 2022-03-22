from math import factorial as fac

n, k = map(int, input().split())

print(int(fac(n)/(fac(k)*fac(n-k))))
