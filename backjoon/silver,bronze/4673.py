number = 1
List = [True for _ in range(10002)]
for i in range(1, 10001):
  falseNum = i
  while True:
    falseNum = sum([int(k) for k in str(falseNum)]) + falseNum
    if falseNum> 10000:
      break
    List[falseNum] = False
for index, element in enumerate(List[1:-1]):
  if element:
    print(index+1)
