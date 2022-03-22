a,b,k = map(int,input().split())

work = (k-b)/(a-b)

print(int(work) if work == int(work) else int(work)+1)