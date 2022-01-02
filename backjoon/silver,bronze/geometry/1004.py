import math
test_case = int(input())
result = []
for _ in range(test_case):
  x1, y1, x2, y2 = map(int, input().split())
  number = int(input())
  cnt1 = 0
  cnt2 = 0
  for _ in range(number):
    cx, cy, r = map(int, input().split())
    distance1 = math.sqrt((cx-x1)**2+(cy-y1)**2)
    distance2 = math.sqrt((cx-x2)**2+(cy-y2)**2)
    if distance1 < r and distance2 < r:
      continue 
    if distance1 < r :
      cnt1 +=1
    if distance2 < r :
      cnt2 +=1

  result.append(cnt1+ cnt2)
    

for i in result:
  print(i)
