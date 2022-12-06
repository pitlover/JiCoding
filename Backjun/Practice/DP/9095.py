'''
3
4
7
10
'''

case = int(input())
case_int = []

for _ in range(case):
    case_int.append(int(input()))

dp = [-1] * 11
dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4

for a in range(4, 11):
    dp[a] = dp[a-1] + dp[a-2]  + dp[a-3]
for _ in case_int:
    print(dp[_])
