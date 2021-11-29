import copy

def recur(array, n):
  if len(array)==n:
    operator_list.append(copy.deepcopy(array))
    return

  array.append(' ')
  recur(array, n)
  array.pop()
  
  array.append('+')
  recur(array, n)
  array.pop()

  array.append('-')
  recur(array, n)
  array.pop()


test_case = int(input())
for _ in range(test_case):
  operator_list =[]
  n= int(input())
  recur([],n-1)
  numbers = [str(i) for i in range(1,n+1)]

  for operator in operator_list:
    string = ''
    for i in range(len(operator)):
      string+= numbers[i]+operator[i]
    string+= numbers[-1]
    if eval(string.replace(' ',''))==0:
      print(string)
  print()