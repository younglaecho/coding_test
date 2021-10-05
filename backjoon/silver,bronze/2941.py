string = input()

num = 0
for i in range(len(string)):
  # print(string[i], string[i-1], string[i-2])

  if string[i] == '=' and i-1>=0 :
    if (string[i-1] == 'c' or string[i-1] == 's'):
      continue
    elif string[i-1] == 'z' :
      if string[i-2] == 'd' and i-2>=0:
        num -= 1
        continue
      else:
        continue
  elif string[i] == '-' and i-1>=0 :
    if string[i-1] == 'd' or string[i-1] == 'c' :
      continue
  elif string[i] == 'j' and i-1>=0 :
    if string[i-1] == 'l' or string[i-1] == 'n':
      continue
  num += 1

print(num)