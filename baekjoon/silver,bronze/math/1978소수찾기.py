n = int(input())
arr = map(int, input().split())

def check_prime(n):
    if n==1:
        return 0
    for i in range(2, int(n**(1/2))+1):
        if n%i==0:
            return 0
    return 1

cnt = 0

for i in arr:
    cnt += check_prime(i)

print(cnt)