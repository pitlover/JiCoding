# 최대값과 최솟값
# Success

def solution(s):
    s = list(map(int, s.split(" ")))
    print(s, [min(s), max(s)])
    return " ".join([str(min(s)), str(max(s))])
