n = int(input())
one = [0,1,1]
zero = [1,0,1]
zero.extend([0]*38)
one.extend([0]*38)

for i in range(3, len(zero)):
  zero[i] = zero[i-2] + zero[i-1]
  one[i] = one[i-2] + one[i-1]


for _ in range(n):
  index = int(input())
  print(zero[index], one[index])