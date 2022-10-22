# 카펫
# Success

import math
def solution(brown, yellow):
    answer = []
    # get_prime
    i = 1
    for a in range(1, int(math.sqrt(yellow))+1):
        if yellow % a == 0:
            result = check(a, yellow // a, brown+yellow)
            if result != -1:
                return result
    # check
def check(m, n, num):
    if (m+2) * (n+2) == num:
        return [n+2, m+2]
    else:
        return -1
