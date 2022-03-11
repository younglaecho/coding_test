n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = set()
visited = [False]*(n+1)


def recur(a, List, depth):
    if depth == m:
        answer.add(tuple(List))
        return

    for i in range(len(arr)):
        if arr[i] >= a:
            List.append(arr[i])
            recur(arr[i], List, depth+1)
            List.pop()


recur(arr[0], [], 0)
answer = list(answer)
answer.sort()
for i in answer:
    for j in i:
        print(j, end=' ')
    print()
