tot, a, b = map(int, input().split())

a = a - 1
b = b - 1

cnt = 0
while True:
    if a == b:
        break
    a = a//2
    b = b//2
    cnt+=1
    
print(cnt)