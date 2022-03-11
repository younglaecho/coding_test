n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()


def recur(List, depth):
    if depth == m:
        print(' '.join(list(map(str, List))))
        return

    for ele in arr:
        if ele not in List:
            List.append(ele)
            recur(List, depth+1)
            List.pop()


recur([], 0)
