n = int(input())

array = []

for _ in range(n):
  array.append(int(input()))

prev = array[0]
left_cnt = 1
right_cnt = 1
for i in range(len(array)):
  if prev < array[i]:
    left_cnt+=1
    prev = array[i]
print(left_cnt)

array.reverse()
prev = array[0]
for i in range(len(array)):
  if prev < array[i]:
    right_cnt+=1
    prev = array[i]
print(right_cnt)