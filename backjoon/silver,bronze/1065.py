n = int(input())

numbers = [i for i in range(1, n+1)]
answer = 0
for number in numbers:
  breaked = False
  if number<=99:
    answer+=1
  else:
    strNum=str(number)
    prev_diff = int(strNum[1])-int(strNum[0])
    for i in range(1, len(strNum)):
      diff = int(strNum[i])-int(strNum[i-1])
      print(diff)
      if diff != prev_diff:
        breaked = True
        break
      else: 
        prev_diff=diff
    if breaked ==False:
      answer+=1
print(answer)