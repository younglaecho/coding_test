n = int(input())
Set = set()
for _ in range(n):
    state = input().split()

    if state[0]=='add':
        Set.add(state[1])
    elif state[0]=='check':
        if state[1] in Set:
            print(1)
        else:
            print(0)
    elif state[0]=='remove':
        if state[1] in Set:
            Set.remove(state[1])
    elif state[0]=='toggle':
        if state[1] in Set:
            Set.remove(state[1])
        else:
            Set.add(state[1])
    elif state[0]=='all':
        Set = {i for i in range(1, 21)}
    elif state[0]=='empty':
        Set = set()
