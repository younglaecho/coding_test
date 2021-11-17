n = input()
breaked = False
if len(n) == 1:
  print('NO')
else:
  for i in range(1, len(n)+1):
    left = 1

    for num in n[:i]:
      left = left * int(num)
    right = 1
    for num in n[i:]:
      right = right * int(num)
    if left == right:
      print('YES')
      breaked = True
      break

  if not breaked:
    print('NO')