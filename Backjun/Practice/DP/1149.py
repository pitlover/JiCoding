'''
3
26 40 83
49 60 57
13 89 99
'''

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))


dp = [[0] * 3 for _ in range(n)]
dp[0] = matrix[0]

for a in range(1, n):
    dp[a][0] = min(dp[a-1][1], dp[a-1][2]) + matrix[a][0]
    dp[a][1] = min(dp[a-1][2], dp[a-1][0]) + matrix[a][1]
    dp[a][2] = min(dp[a - 1][0], dp[a - 1][1]) + matrix[a][2]

print(min(dp[-1]))