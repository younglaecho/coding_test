import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
memo = [[0 for _ in range(k+1)] for _ in range(n+1)]

load = [[0, 0]]

for _ in range(n):
  load.append(list(map(int, input().split())))

for i in range(1, n+1):
  weight = load[i][0]
  prior = load[i][1]
  for j in range(1, k+1):
    if j >= weight:
      memo[i][j] = max(memo[i-1][j], memo[i-1][j-weight]+prior)
    else:
      memo[i][j] = memo[i-1][j]

print(memo[n][k])


# Dict = {0: 0}

# load = [[0, 0]]

# for _ in range(n):
#   load.append(list(map(int, input().split())))

# for i in range(n):
#   weight = load[i][0]
#   prior = load[i][1]
#   temp = {}
#   for w, p in Dict.items():
#     if weight+w <= k and  prior+p > Dict.get(weight+w, 0):
#       temp[weight+w] = prior + p
#   Dict.update(temp)

# print(Dict)