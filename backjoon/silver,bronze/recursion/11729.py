result = []

def hanoi(n, f, b, t):
  if n == 1:
    result.append([f,t])  # 원판이 하나만 남았을 때는 가야할 곳으로 바로 갈 수 있다.
  else:
    hanoi(n-1, f, t, b)   # 옮겨야 할 가장 큰 원판이 한번만 움직여도 될 때를 만들어주는 상태
    result.append([f,t])  # 옮겨야 원판 중 가장 큰 원판을 옮김
    hanoi(n-1, b, f, t)   # 가장 큰 원판을 옮긴 뒤에는 나머지 원판들을 그 위로 옮김

n = int(input())
print(2**n - 1)
hanoi(n, 1, 2, 3)
for i in result:
  print(*i)