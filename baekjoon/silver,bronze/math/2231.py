n = int(input())

for i in range(1, n):
    str_i = str(i)
    number = i
    for j in str_i:
        number+=int(j)
    if n ==number:
        print(i)
        exit()
print(0)