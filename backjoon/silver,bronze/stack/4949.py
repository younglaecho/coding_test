while True:
  string = input()
  if string=='.':
    break

  stack = []
  for char in string:
    if char == '[' or char == '(':
      stack.append(char)
    if char == ']':
      if stack:
        if stack[-1] == '[':
          stack.pop()
        else:
          print('no')
          break
      else:
        print('no')
        break
    elif char==')':
      if stack:
        if stack[-1] == '(':
            stack.pop()
        else:
          print('no')
          break
      else:
        print('no')
        break
  else:
    if stack:
      print('no')
    else:
      print('yes')