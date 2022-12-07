'''
10
'''
n = int(input())
dp = [-1] * (n + 1)

if n == 1:
    print(0)
    exit()

elif n == 2 or n == 3:
    print(1)
    exit()

dp[0], dp[1], dp[2], dp[3] = 10 ** 6, 1, 1, 1

for a in range(4, n + 1):
    a_div_2 = a // 2 if a % 2 == 0 else 0
    a_div_3 = a // 3 if a % 3 == 0 else 0
    dp[a] = min(dp[a - 1], dp[a_div_2], dp[a_div_3]) + 1
print(dp[-1])
