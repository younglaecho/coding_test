n = int(input())

arr = []
for i in range(n):
    string = input()
    arr.append(string)

answer = ''
for i in range(len(arr[0])):
    breaked = False
    if n == 1:
        answer = arr[0]
    else:
        for j in range(n-1):
            if arr[j][i] != arr[j+1][i]:
                answer += '?'
                breaked = True
                break
        if breaked:
            continue
        answer += arr[j][i]
print(answer)
