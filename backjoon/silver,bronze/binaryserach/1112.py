L, K, C = map(int, input().split())
cuts = [0, L] + list(map(int, input().split()))
cuts.sort()

def solution(mid):
  cut_start = L 
  prev = []
  cnt = 0
  first = 0
  for i in range(len(cuts)-1, -1, -1):
    diff = cuts[i]-cuts[i-1]
    total = cut_start-cuts[i]

    if diff > mid:
      return 10001, 0
    elif total > mid:
      prev.append(cuts[i+1])
      cut_start = cuts[i+1]
      cnt += 1
    else:
      continue
  if cnt < C:
    first = cuts[1] 
  else:
    first = prev[-1]

  return cnt, first


start = 0
end = L
answer = 0
first_cut = 0
while start <= end:
  mid = (start+end)//2
  
  cnt, first = solution(mid)

  if cnt > C:
    start = mid + 1
  else:
    end = mid - 1
    answer = mid
    first_cut = first

print(answer, first_cut)
