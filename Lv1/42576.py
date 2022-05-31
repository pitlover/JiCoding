# 완주하지 못한 선수
# Success

def solution(participant, completion):
    count = dict.fromkeys(participant, 0)
    for a in participant:
        count[a] += 1
    for a in completion:
        count[a] -=1
    for k, v in count.items():
        if v == 1:
            return k