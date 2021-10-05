n = int(input())

non_group = 0
for _ in range(n):
  string = input()
  prev_alpha = ''
  dict = {}
  for alpha in string:
    if prev_alpha != alpha:
      if alpha in dict: 
        non_group +=1
        break
      dict[alpha] = 1
    else:
      dict[alpha] += 1
    prev_alpha = alpha

print(n-non_group)