'''
1
'''

n = int(input())

dp = [(0, 0)] * (n+1)

dp[0] = (1, 0)
dp[1] = (1, 0)

for a in range(1, n+1):
    total = dp[a-1][0] + 2 * dp[a-1][1]
    dp[a] = (dp[a-1][1], total-dp[a-1][1])

a, b = dp[-1]
print(f"{a} {b}")