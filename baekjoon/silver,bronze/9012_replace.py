n = int(input())

for _ in range(n):
  string = input()
  for _ in range(int(len(string)+1)):
    string = string.replace('()', '')
  print('NO' if string else 'YES')