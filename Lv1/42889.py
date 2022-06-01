# 실패율
# Little Help

def solution(N, stages):
    total = len(stages)
    answer = 0
    stages.sort()
    tmp = [_ for _ in range(1, N + 1)]
    dict_ = dict.fromkeys(tmp, 0)
    for a in stages:
        if a == N + 1:
            continue
        dict_[a] += 1
    result = {}

    for k, v in dict_.items():
        if total == 0:
            result[k] = 0
            continue
        result[k] = v / total
        total -= v

    final = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

    answer = list(final.keys())
    return answer