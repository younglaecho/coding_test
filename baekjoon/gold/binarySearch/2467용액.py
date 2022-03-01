n = int(input())

arr = list(map(int, input().split()))

start = 0
end = len(arr)-1
min_sum = abs(arr[start]+ arr[end])
min_index = [start, end]

while start<end:
  Sum = arr[start] + arr[end]
  if abs(Sum) < min_sum:
    min_sum = abs(Sum)
    min_index = start, end
  if Sum>0:
    end-=1
  elif Sum<0:
    start+=1
  else:
    break

print(arr[min_index[0]], arr[min_index[1]])
  
