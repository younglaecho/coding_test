for _ in range(int(input())):
  left_stack = []
  right_stack = []
  string = input()

  for i in string:
    if i == '<':
      if len(left_stack):
        right_stack.append(left_stack.pop())
    elif i == '>':
      if len(right_stack):
        left_stack.append(right_stack.pop())
    elif i == '-':
      if len(left_stack):
        left_stack.pop()
    else:
      left_stack.append(i)
  left_stack.extend(reversed(right_stack))
  print(''.join(left_stack))