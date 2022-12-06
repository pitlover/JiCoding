n = int(input())

dp = [-1] * (5001)
dp[3] = 1
dp[5] = 1

for num in range(6, n + 1):
    if dp[num - 3] != -1 and dp[num - 5] != -1:
        dp[num] = min(dp[num - 3], dp[num - 5]) + 1
    elif dp[num - 3] == -1 and dp[num - 5] != -1:
        dp[num] = dp[num - 5] + 1
    elif dp[num - 3] != -1 and dp[num - 5] == -1:
        dp[num] = dp[num - 3] + 1

print(dp[n])
