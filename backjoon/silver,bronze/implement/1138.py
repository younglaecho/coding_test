n = int(input())

input_arr = list(map(int, input().split()))
result = [0]*n
for i in range(1,n+1):
  taller = input_arr[i-1]
  cnt = 0
  for j in range(n):
    if cnt == taller and result[j]==0:
      result[j] = i
      break
    elif result[j] == 0:
      cnt+=1


print(*result)
      
  