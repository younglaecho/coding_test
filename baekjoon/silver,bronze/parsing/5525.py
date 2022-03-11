n = int(input())
t = int(input())

String = input()

cnt = 0
tmp = 0
i = 1

while i < len(String)-1: 
    if String[i-1] == 'I' and String[i]=='O' and String[i+1]=='I':
        tmp += 1
        i += 2
        if tmp == n:
            cnt += 1
            tmp -= 1
    else:
        tmp = 0
        i += 1
print(cnt)