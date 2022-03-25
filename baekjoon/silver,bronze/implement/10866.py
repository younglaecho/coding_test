from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()

for _ in range(n):
    state = input().split()

    if state[0]=="push_back":
        q.append(state[1])

    elif state[0]=="push_front":
        q.appendleft(state[1])

    elif state[0]=="front":
        print(q[0] if len(q) else -1)

    elif state[0]=="back": 
        print(q[-1] if len(q) else -1)

    elif state[0]=="empty":
        print(0 if len(q) else 1)

    elif state[0]=="pop_front":
        print(q.popleft() if len(q) else -1)

    elif state[0]=="pop_back":
        print(q.pop() if len(q) else -1)

    elif state[0]=="size":
        print(len(q))
