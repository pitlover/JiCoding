'''
1
'''
n = int(input())

n = 9 * (10 ** (n - 1))
print(n)

dp = [0] * (n + 1)
dp[1:10] = [1 for _ in range(1, 10)]

def sol(num):

    # chk
    
    if stair:
        return 1
    else:
        return 0

for a in range(10, n+1):
    dp[a] = dp[a-1] + sol(a)
