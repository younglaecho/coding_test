import sys
n = int(input())
stack = []

commands = []

for _ in range(n):
  commands.append(input())
for command in commands:
  if command == 'pop':
    if len(stack)==0:
      print('-1')
    else:
      print(stack.pop())

  elif command == 'size':
    print(len(stack))
  
  elif command == 'top':
    if len(stack)==0:
      print('-1')
    else:
      print(stack[-1])
  
  elif command == 'empty':
    if len(stack)==0:
      print('1')
    else:
      print('0')
  
  else:
    stack.append(command[5:])