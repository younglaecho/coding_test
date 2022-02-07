n = input()

init = n

cnt = 0
if n == '0':
    print('1')
else:
    while True:
        if int(n) < 10:
            right = n
            n = str(int(n)*10)
        else:
            right = n[1]
        add_right = str(int(n[0]) + int(n[1]))
        if right == '0':
            n = add_right[len(add_right)-1]
        else:
            n = right + add_right[len(add_right)-1]

        cnt += 1
        if init == n:
            break
    print(cnt)

