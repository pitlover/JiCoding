# K진수에서 소수 개수 구하기
# Success

import math

def check_prime(data):
    check = int(math.sqrt(data))
    print(check)
    for a in range(2, check + 1):
        if data % a == 0:
            return 0
    return 1


def solution(n, k):
    k_convert = []
    while (n > 1):
        k_convert.append(n % k)
        n = n // k
    k_convert.append(n)
    k_convert = k_convert[::-1]
    # print(k_convert)
    k_convert = "".join(str(a) for a in k_convert)
    # print(k_convert.split("0"))
    answer = 0
    for data in k_convert.split("0"):
        if data != '' and data != "1":
            answer += check_prime(int(data))

    return answer