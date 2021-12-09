n = int(input())
arr = list(map(int, input().split()))
arr1 = list(map(lambda x:[x,0], arr))
cnt = 0
arr.sort()
arr = set(arr)
for ele in arr:
  for i in range(len(arr1)):
    if arr1[i][0]==ele:
      arr1[i][1]=cnt
      cnt+=1

for ele1 in arr1:
  print(ele1[1], end=' ')