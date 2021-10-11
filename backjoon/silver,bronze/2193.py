n = int(input())

dp = [1,1]*45

for i in range(2, len(dp)):
  dp[i] = dp[i-2]+dp[i-1]

print(dp[n-1])