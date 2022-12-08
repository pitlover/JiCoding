'''
10
10 -4 3 1 5 6 -35 12 21 -1
'''
n = int(input())
dp = list(map(int, input().split()))
for i in range(1, n):
    dp[i] = max(dp[i], dp[i] + dp[i-1])
print(max(dp))