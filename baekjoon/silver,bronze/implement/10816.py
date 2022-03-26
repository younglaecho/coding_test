from collections import Counter
n = int(input())
List = Counter(map(int, input().split()))

m = int(input())
inputs = list(map(int, input().split()))

result = []
for ele in inputs:
    result.append(List[ele])

print(' '.join(map(str, result)))