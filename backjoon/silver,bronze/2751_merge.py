def merge(array):
  if len(array)==1:
    return array
  mid = len(array)//2
  left = merge(array[:mid])
  right = merge(array[mid:])

  i,j,k = 0,0,0
  while i< len(left) and j<len(right):
    if left[i]>right[j]:
      array[k] = right[j]
      j+=1
    else:
      array[k] = left[i]
      i+=1
    k+=1
  if i==len(left):
    while j< len(right):
      array[k] = right[j]
      j+=1
      k+=1
  if j== len(right):
    while i< len(left):
      array[k] = left[i]
      i+=1
      k+=1
  return array



n = int(input())

arr = []

for _ in range(n):
  arr.append(int(input()))

for i in merge(arr):
  print(i)

