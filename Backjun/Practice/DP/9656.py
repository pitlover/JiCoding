'''
4
'''
n = int(input())
dp = [0] * (n+1)

if n == 1:
    print("CY")
    exit()
elif n == 2:
    print("SK")
    exit()
dp[0] = "CY"
dp[1] = "CY"
dp[2] = "SK"
dp[3] = "CY"

for a in range(4, n+1):
    dp[a] = "SK" if dp[a-3] == "CY" else "CY"
print(dp[-1])

# 걍 홀수이면 CY 이고 짝수이면 SK 임.. 넘 어렵게 생각한듯