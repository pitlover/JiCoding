'''
3
'''

n = int(input())
dp = [0] * (n+1)
if n == 1 or n == 2:
    print(1)
    exit()
dp[0], dp[1], dp[2] = 1, 1, 1

for a in range(3, n+1):
    dp[a] = dp[a-1] + dp[a-2]

print(dp[-1])