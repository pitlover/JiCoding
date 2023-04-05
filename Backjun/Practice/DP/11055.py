'''
10
1 100 2 50 60 3 5 6 7 8
'''
n = int(input())
num = list(map(int, input().split()))
dp = num[:]
for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], num[i] + dp[j])

print(max(dp)) 