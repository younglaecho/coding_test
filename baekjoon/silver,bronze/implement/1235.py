test_case = int(input())
numbers = [input() for _ in range(test_case)]
arr = []

for i in range(1, 101):
  for number in numbers:
    if number[-i:] not in arr:
      arr.append(number[-i:])
    else:
      break
  else:
    print(i)
    break
  
