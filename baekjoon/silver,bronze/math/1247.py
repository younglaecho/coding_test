result = []

for _ in range(3):
    n = int(input())
    total = 0
    for _ in range(n):
        total += int(input())
    
    if total > 0:
        result.append('+')
    elif total==0:
        result.append('0')
    else:
        result.append('-')

for ele in result:
    print(ele)