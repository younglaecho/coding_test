string = input()
substr = input()

cnt = 0

string=string.replace(substr, '*')
for i in string:
  if i == '*':
    cnt+=1
print(cnt)