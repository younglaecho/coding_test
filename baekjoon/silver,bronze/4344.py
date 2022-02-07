n = int(input())

for _ in range(n):
  scores = list(map(int, input().split()))
  student_number = scores[0]
  sum = 0
  for i in range(1, scores[0] + 1):
    sum += scores[i]
  avg = sum/student_number
  num = 0
  for i in range(1, scores[0] + 1):
    if scores[i] > avg:
      num+=1
  print('%0.3f' % (num*100/student_number)+'%')