
n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()


def recur(a, List, depth):
    if depth == m:
        print(' '.join(list(map(str, List))))
        return

    for ele in arr:
        if ele >= a:
            a = ele
            List.append(ele)
            recur(a, List, depth+1)
            List.pop()


recur(arr[0], [], 0)
