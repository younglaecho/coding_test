n = int(input())

arr = []

for _ in range(n):
  score = input().split()
  score[1] = int(score[1])
  score[2] = int(score[2])
  score[3] = int(score[3])
  arr.append(score)

arr.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in arr:
  print(i[0])