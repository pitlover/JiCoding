# 직사각형 별 찍기
# Success

n, m = map(int, input().strip().split(' '))

for _ in range(m):
    print("*" * n)

# 없는 숫자 더하기
# Success

def solution(numbers):
    return 45 - sum(numbers)

# 음양 더하기
# Success

def solution(absolutes, signs):
    answer = 0
    for i, a in enumerate(signs):
        if a:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

# 내적
# Success

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

# 약수의 개수와 덧셈
# Success

import math
def is_div(num):
    count = 0
    for a in range(1, num + 1):
        if num % a == 0:
            count += 1
    return count


def solution(left, right):
    answer = 0
    for a in range(left, right + 1):
        temp = is_div(a)
        if temp % 2 == 0:
            answer += a
        else:
            answer -= a
    return answer