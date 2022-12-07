'''
3
2 2
1 5
13 29
'''

result = []

n = int(input())
dp = [[1] * 30 for _ in range(30)]


for a in range(1, 30):
    for b in range(1, a):
        dp[a][b] = dp[a-1][b] + dp[a-1][b-1]


for _ in range(n):
    x, y = map(int, input().split())
    result.append(dp[y][x])

for _ in result:
    print(_)

'''
nCk = n-1Ck + n-1Ck-1
dp[n][k] = dp[n-1][k] + dp[n-1][k-1]


'''