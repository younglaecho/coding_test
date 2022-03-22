test_case = int(input())


for _ in range(test_case):
    w, h, n = map(int, input().split())

    floor = n % w if n % w else n % w + w
    a = n // w + 1 if n % w else n // w 

    print(str(floor)+'0'+str(a)if len(str(a)) <2 else str(floor)+str(a))