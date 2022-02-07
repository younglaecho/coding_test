from math import gcd
n,m = map(int, input().split())
print(gcd(n,m))
print(m*n//gcd(m,n))