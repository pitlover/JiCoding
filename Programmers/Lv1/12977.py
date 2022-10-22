# 소수 만들기
# Success

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