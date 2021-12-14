def solution(priorities, location):
    arr = []
    cnt = 0
    
    for i in range(len(priorities)):
        arr.append([priorities[i],i])
    while True:
        first = arr.pop(0)
        if len(arr)==0:
            cnt+=1
            return cnt
        if first[0] < max(arr, key = lambda x:x[0])[0]:
            arr.append(first)
        else:
            cnt+=1
            if first[1] == location:
                return cnt