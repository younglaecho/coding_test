def solution(n, left, right):
    arr = [0]*(n**2)
    start_num = left
    last_num = right
    if n ==1:
        return [1]
    for i in range(left, right+1):
        col = i // n
        row = i % n
        arr[i] = max(col,row)+1

    return arr[left:right+1]

print(solution(5, 1,3))