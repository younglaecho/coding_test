test_case1 = int(input())

for test_case in range(1, test_case1+1):
  K, N, M = map(int, input().split())
  stations = list(map(int, input().split()))
  real_K = K
  i = 0
  cnt = 0
  while True:
    K -=1
    i+=1
    if i ==N:
      print(f"#{test_case} {cnt}")
      break
    if K == 0:
      for j in range(i, i-real_K,-1):
        if j in stations:
          i = j
          cnt+=1
          K = real_K
          break
      else:
        print(f"#{test_case} {0}")
        break
