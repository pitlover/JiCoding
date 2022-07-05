# 숫자의 표현
# Success

def solution(n):
    if n in [1, 2]:
        return 1
    elif n == 3:
        return 2
    
    dp = [1 for _ in range(n+1)]
    tmp = [3, 5, 6]
    dp[3] = 2
    for a in range(4, (n+1)//2+1):
        tmp.insert(0, 0)
        for index in range(len(tmp)):
            tmp[index] += a
            if tmp[index] <= n:
                dp[tmp[index]] += 1
                continue
            break   
    print(dp)
    return dp[n]
