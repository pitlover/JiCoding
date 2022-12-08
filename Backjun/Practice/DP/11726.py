'''
2
'''

n = int(input())

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()

dp = [0] * (n+1)
dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3
for i in range(4, n+1):
    dp[i] = (dp[i-2] % 10007 * 2 + dp[i-3] % 10007) % 10007

print(dp[-1] % 10007)