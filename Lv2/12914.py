# 멀리 뛰기
# Success

def solution(n):
    dp = [0 for _ in range(n+1)]
    
    dp[0], dp[1] = 1, 2
    
    if n == 1:
        return 1
    
    for a in range(2, n+1):
        dp[a] = (dp[a-1] + dp[a-2] ) % 1234567
        
    return dp[n-1]%1234567
