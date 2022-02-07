n, l = map(int, input().split())

answers = []
exist = False
for i in range(int(n/2)+1,l, -1):
  answer =''
  if (n/i)%2==1 and n%i==0:
    exist = True
    if int(n/i/2)>= 50:
      break
    for j in range(i - int(n/i/2), i + int(n/i/2)+1):
      answer += str(j) + ' '
    if answer[0] != '-':
      answers.append(answer)
    
  


if len(answers)==0:
  print(-1)
else:
  length=[]
  for i in answers:
    length.append(len(i))
  index = length.index(min(length))
  result = answers[index]
  print(result[:len(result)-1])

