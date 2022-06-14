# H-Index
# Success

def solution(citations):
    answer = 0
    for x in range(len(citations), -1, -1):  # x-1
        result = 0
        for a in citations:
            if x <= a:
                result += 1
        if x <= result:
            return x

    return 0