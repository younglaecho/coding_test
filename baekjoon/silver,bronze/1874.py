n = int(input())

List = [int(input()) for _ in range(n)]
stack = []
result = []
for i in range(1,n+1):
  stack.append(i)
  result.append('+')
  while List[0]==stack[len(stack)-1]:
    List.pop(0)
    stack.pop()
    result.append('-')
    if len(stack)==0:
      break
    
if len(stack)==0:
  for i in result:
    print(i)
else:
  print('NO')