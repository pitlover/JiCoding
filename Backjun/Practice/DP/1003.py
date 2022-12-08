'''
3
0
1
3
'''

n = int(input())
chk = []

for _ in range(n):
    chk.append(int(input()))
dp = [-1] * (max(chk)+1)
if n == 1:
    if chk[0] == 0:
        print(1, 0)
        exit()
    elif chk[0] == 1:
        print(0, 1)
        exit()
dp[0] = (1, 0)
dp[1] = (0, 1)
for i in range(2, len(dp)):
    dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1]+dp[i-2][1])

for a in chk:
    print(dp[a][0], dp[a][1])