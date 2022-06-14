# 타겟 넘버
# Success

def solution(numbers, target):
    arr = [0]
    for a in range(len(numbers)):
        tmp = []
        for b in arr:
            tmp.append(b+numbers[a])
            tmp.append(b-numbers[a])
        arr = tmp
    return arr.count(target)