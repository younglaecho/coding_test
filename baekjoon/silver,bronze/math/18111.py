from collections import defaultdict
n, m, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
Dict = defaultdict(int)

Max = 0
Min = 256
for i in range(n):
    for j in range(m):
        Dict[matrix[i][j]]+=1
        Max = max(Max, matrix[i][j])
        Min = min(Min, matrix[i][j])

import copy

dif = Max - Min
results = []

for i in range(dif+1):
    tmp = b
    result = 0

    new_dict = copy.deepcopy(Dict)
    for x in range(i):
        new_dict[Max-x-1] += new_dict[Max-x]
        result += new_dict[Max-x]* 2
        tmp += new_dict[Max-x]
        new_dict[Max-x] = 0
    
    for x in range(dif-i):
        new_dict[Min+x+1] += new_dict[Min+x]
        result += new_dict[Min+x]
        tmp -= new_dict[Min+x]
        new_dict[Min+x] = 0

    if tmp >=0:
        results.append((result, i))

answer = min(results, key=lambda x: x[0])
print(answer[0],Max-answer[1])
