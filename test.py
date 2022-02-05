import random

temp = ''
for i in range(100):
  for j in range(100):
    temp += str(random.randint(0,1))
  temp+='\n'

print(temp)