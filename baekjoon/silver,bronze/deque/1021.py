n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
elements = list(map(int, input().split()))
result = []
while elements:
  element = elements.pop(0)
  # print(arr, element)
  right = arr[arr.index(element):]
  left = arr[:arr.index(element)]
  # print(right)
  # print(left)
  if len(right)> len(left) :
    arr = right + left
    result.append(len(left))
    arr.pop(0)
  else:
    arr = right + left
    result.append(len(right))
    arr.pop(0)


print(sum(result))