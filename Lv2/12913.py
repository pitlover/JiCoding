# 땅 따먹기
# Success


def solution(land):
    dp = [[0, 0, 0, 0] for _ in range(len(land))]
    dp[0] = land[0]
    
    for a in range(1, len(land)):
        for b in range(4):
            tmp = dp[a-1][:]
            del tmp[b]
            dp[a][b] = max(tmp) + land[a][b]
    return max(dp[-1])
