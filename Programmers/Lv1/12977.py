# 소수 만들기
# Success

'''
# Old
def is_prime(num):
    import math
    for a in range(2, int(math.sqrt(num))+1):
        if num % a == 0:
            return -1
    return 1
def solution(nums):
    answer = 0
    check_list = []
    for a in range(len(nums)-2):
        for b in range(a+1, len(nums)-1):
            for c in range(b+1, len(nums)):
                check_list.append(nums[a]+nums[b]+nums[c])
    for a in check_list:
        if is_prime(a) == 1:
            answer += 1
    return answer
'''
import math
from itertools import combinations


def is_prime(num):
    for a in range(2, int(math.sqrt(num)) + 1):
        if num % a == 0:
            return False
    return True


def solution(nums):
    combs = combinations(nums, 3)
    result = 0
    for comb in combs:
        if is_prime(sum(comb)):
            result += 1

    return result


solution([1, 2, 3, 4])
solution([1, 2, 7, 6, 4])
