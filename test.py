
def solution(k, a, b):
    answer = sum(a)
    for i in range(k):
        min_a = min(a)
        max_b = max(b)
        answer += max_b - min_a
        a.remove(min_a)
        b.remove(max_b)
    return answer

k = 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]
answer = solution(k, a, b)
print(answer)