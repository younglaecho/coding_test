n = int(input())

scores = list(map(int, input().split()))

max_value= max(scores)

for i in range(n):
  scores[i] = scores[i]/max_value * 100

print(sum(scores)/n)