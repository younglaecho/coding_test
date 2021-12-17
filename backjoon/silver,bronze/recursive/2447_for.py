def mulThree(star):
  length = len(star)
  arr = []
  for i in range(length*3):
    if i % length == 1:
      arr.append(star[i%length]+" "*length+star[i%length])
    else:
      arr.append(star[i%length]*3)
  return arr

star = ['***',
        '* *',
        '***']
n = int(input())
k = 0
while n!=3:
  n //= 3
  k+=1

print(k)
for _ in range(k):
  star = mulThree(star)

for i in star:
  print(i)