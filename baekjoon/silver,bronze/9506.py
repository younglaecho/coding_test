def solution(number):
  numbers = []
  for i in range(1, int(number/2)+1):
    if number % i == 0:
      numbers.append(i)
  if sum(numbers) == number:
    numbers = ' + '.join(map(str, numbers))
    print(str(number) + ' = ' + numbers)
  else:
    print(str(number) + ' is NOT perfect.')
while True:
  n = int(input())
  if n == -1:
    break
  solution(n)

