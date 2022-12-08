'''
6
6
10
13
9
8
1
'''

n = int(input())
grape = []
for _ in range(n):
    grape.append(int(input()))

dp = [0] * n

if n == 1 or n == 2:
    print(sum(grape))
    exit()

dp[0], dp[1] = grape[0], grape[0] + grape[1]
dp[2] = max(grape[1] + grape[2], grape[0] + grape[2], dp[1])

if n == 3:
    print(dp[2])
    exit()

for a in range(3, n):
    dp[a] = max(dp[a-1], dp[a-2] + grape[a], dp[a-3] + grape[a-1] + grape[a])
print(dp[-1])