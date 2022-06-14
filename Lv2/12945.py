# 피보나치 수 DP
# Success

def solution(n):
    fibo = [0 for _ in range(n + 1)]
    fibo[0], fibo[1], fibo[2] = 0, 1, 1

    for a in range(3, n + 1):
        fibo[a] = fibo[a - 1] + fibo[a - 2]

    return fibo[-1] % 1234567