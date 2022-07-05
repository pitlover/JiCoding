# 숫자블록
# Success

def get_prime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    i = 2
    max_ = 1
    while i**2 <= n:
        if n % i == 0 and n // i <= 10000000:
            return n//i
        i+=1
    return max_

def solution(begin, end):
    result = [0]
    for a in range(begin, end+1):
        result.append(get_prime(a))      
    return result[1:]
