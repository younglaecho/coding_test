number_light = {
    '0':[1, 1, 1, 0, 1, 1, 1],
    '1':[0, 0, 1, 0, 0, 1, 0],
    '2':[1, 0, 1, 1, 1, 0, 1],
    '3':[1, 0, 1, 1, 0, 1, 1],
    '4':[0, 1, 1, 1, 0, 1, 0],
    '5':[1, 1, 0, 1, 0, 1, 1],
    '6':[1, 1, 0, 1, 1, 1, 1],
    '7':[1, 1, 1, 0, 0, 1, 0],
    '8':[1, 1, 1, 1, 1, 1, 1],
    '9':[1, 1, 1, 1, 0, 1, 1],
    '*':[0, 0, 0, 0, 0, 0, 0]
}

test_case = int(input())

for _ in range(test_case):
    a, b = input().split()

    long = max(len(a), len(b))
    a = (long-len(a))*'*' + a
    b = (long-len(b))*'*' + b
    
    cnt = 0

    for i in range(long):
        a_light = number_light[a[i]]
        b_light = number_light[b[i]]
        for j in range(7):
            if a_light[j] != b_light[j]:
                cnt+=1
    print(cnt)