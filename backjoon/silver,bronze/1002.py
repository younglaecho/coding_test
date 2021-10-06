import math
a = int(input())
for i in range(a):
    x1,y1,r1,x2,y2,r2 = map(float, input().split())
    distance = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    if r1 < r2 :
        r1, r2 = r2, r1
    if distance == 0 :
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif r1 > distance:
        if r1 - r2 > distance:
            print(0)
        elif r1 - r2 == distance:
            print(1)
        else:
            print(2)
    elif distance > r1 + r2:
        print(0)
    elif distance == r1 + r2:
        print(1)
    else:
        print(2)