# 소수찾기
# Success

from itertools import permutations
def is_prime(n):
    if n == 1:
        return False
    x = 2
    while x*x <= n:
        if n%x == 0:
            return False
        x += 1
    return True

def remove_zero(i) -> int: ## [0, 0, 1, 1, 0]
    pt = 0
    if sum(i) == 0:
        return 1
        
    for a in range(len(i)):
        if i[a] != '0':
            result = i[a:]
            return int("".join(map(str, result)))
    
    return int("".join(map(str, i)))
    
def solution(numbers):
    answer = []
    
    for subset in range(1, 1 << len(numbers)): # 00, 01, 10, 11
        tmp = []
        for j in range(len(numbers)):
            if subset & (1 << j):
                tmp.append(numbers[j])
        check = list(permutations(tmp))
        for i in check:
            i = list(map(int, i))
            i = remove_zero(i)
            
            if is_prime(i):
                answer.append(i)
    answer = len(set(answer))
    
    return answer
