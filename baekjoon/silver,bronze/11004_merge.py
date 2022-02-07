def merge(array):
  if len(array)<=1:
    return array

  mid = len(array)//2
  left = merge(array[mid:])
  right = merge(array[:mid])

  i, j, k = 0, 0, 0
  while i < len(left) and j< len(right):
    if left[i]< right[j]:
      array[k] = left[i]
      i+=1
    else:
      array[k] = right[j]
      j+=1
    k+=1
  if i==len(left):
    while j<len(right):
      array[k]=right[j]
      k+=1
      j+=1
  if j==len(right):
    while i<len(left):
      array[k]=left[i]
      k+=1
      i+=1
  return array
  


n,m = map(int, input().split())

nums = list(map(int, input().split()))

nums = merge(nums)

print(nums[m-1])