# 숫자의 표현
# 15: Runtime, 18 : Fail

def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[0], dp[1], dp[2] = 1, 1, 1
    tmp = [3, 2]
    for a in range(3, len(dp)):
        tmp.append(0)
        for b in range(len(tmp)-1, -1, -1):
            tmp[b] += a
            if tmp[b] <= n:
                dp[tmp[b]] += 1
            else:
                break
        if tmp[-2] > n:
            break
    return dp[-1] + 1

## another sol

def solution(n):
    if n == 1 and n == 2:
        return 1
    elif n == 3:
        return 2
    
    dp = [1 for _ in range(n+1)]
    tmp = [3, 5, 6]
    dp[1], dp[2], dp[3] = 1, 1, 2
    for a in range(4, (n+1)//2+1):
        tmp.insert(0, 0)
        for index, b in enumerate(tmp):
            tmp[index] += a
            if tmp[index] <= n:
                dp[tmp[index]] += 1
            else:
                break
                
    return dp[n]
