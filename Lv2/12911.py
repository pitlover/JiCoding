# 다음 큰 숫자
# Success

def solution(n):
    count_one = bin(n).count("1")
    for a in range(n+1, 1<<20):
        if bin(a).count("1") == count_one:
            return a
