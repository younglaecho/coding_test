string = input()
substr = input()

cnt = 0
i = 0

while len(string) - i >=len(substr):
  if string[i:i+len(substr)] == substr:
    cnt+=1
    i += len(substr)
  else:
    i +=1
print(cnt)