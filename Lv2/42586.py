# 기능 개발
# Success except testcase 11

from math import ceil

def solution(progresses, speeds):
    remain = []
    for a in range(len(progresses)):
        remain.append(ceil((100-progresses[a])//float(speeds[a])))
    tmp = []
    bottleneck = remain[0]
    answer = [0]
    for a in range(1, len(remain)):
        if bottleneck < remain[a]:
            bottleneck = remain[a]
            answer.append(a)
    answer.append(len(remain))   
    tmp = []
    for a in range(len(answer)-1):
        tmp.append(answer[a+1] - answer[a])
    print(tmp)
    return tmp
