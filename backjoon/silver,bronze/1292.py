a, b = map(int, input().split())
arr = []
cnt = 0
num = 1

while True:
  for _ in range(num):
    arr.append(num)
    cnt+=1
  num +=1
  if cnt >b:
    break
print(sum(arr[(a-1):(b)]))
