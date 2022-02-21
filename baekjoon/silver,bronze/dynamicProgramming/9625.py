n = int(input())

dp = [1,0]

for _ in range(n):
  dp[0], dp[1] = dp[1], dp[0]+dp[1]

print(dp[0], dp[1])