n = int(input())

for _ in range(n):
  string = input()
  stack = []
  for alpha in string:
    if stack and stack[-1]== '(' and alpha ==')':
      stack.pop()
    else:
      stack.append(alpha)
  print("NO" if stack else "YES")