n = int(input())
arr = []

for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y, i))

result = []
for i in range(len(arr)):
    number = 1
    for j in range(len(arr)):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            number+=1
    
    result.append(number)

print(' '.join(map(str,result)))