n, c = list(map(int, input().split()))

array = []
for _ in range(n):
  array.append(int(input()))
array = sorted(array)

start = 1                         # gap의 최소치
end = array[-1]-array[0]          # gap의 최대치
result = 0                        
while (start<=end):
  cnt = 1                         # 첫번째 항으로 하나를 카운트한다.
  gap = (end+start)//2            # gap이 될 수 있는 후보중에서 중간으로 시작한다.
  value = array[0]                # 첫번째 항을 기준 값으로 정한다.

  for i in range(1, len(array)):  # 첫번째는 먹고 들어갔으니 두번째 항부터 시작한다.
    if array[i]>=value+gap:       # 정한 gap이후의 값을 만나면,
      cnt+=1                      # 개수를 추가하고
      value= array[i]             # 기준 값을 그 값으로 정한다.

  if cnt >= c:                    # 해당하는 gap으로 세어진 개수가 우리가 목표한 값보다 크거나 같으면,
    start = gap+1                 # 후보군 범위 중 현재 만족하는 gap 위에서 탐색하기 위해 start를 gap+1로 설정한다.
    result = gap                  # 정답의 후보가 되므로 result에 일단 값을 저장한다.
  else:                           # 해당하는 gap으로 세어진 개수가 우리가 목표한 값보다 작으면,
    end = gap-1                   # 후보군 범위 중 현재 만족하지 않는 gap 아래에서 탐색하기 위해 end를 gap-1로 설정한다.
                                  # 이를 end가 start를 따라잡을 때까지 실시한다.(while)

print(result)