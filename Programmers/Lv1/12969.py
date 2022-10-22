# 직사각형 별 찍기
# Success

n, m = map(int, input().strip().split(' '))

for _ in range(m):
    print("*" * n)

# 없는 숫자 더하기
# Success

def solution(numbers):
    return 45 - sum(numbers)
