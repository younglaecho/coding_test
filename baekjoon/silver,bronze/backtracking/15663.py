n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

answer = set()
visited = [False]*(n+1)


def recur(List, depth):
    if depth == m:
        answer.add(tuple(List))
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            List.append(arr[i])
            recur(List, depth+1)
            visited[i] = False
            List.pop()


recur([], 0)
answer = list(answer)
answer.sort()
for i in answer:
    for j in i:
        print(j, end=' ')
    print()
