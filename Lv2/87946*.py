# 피로도
# Very Important !!

from collections import deque


def solution(k, dungeons):
    L, n, dp = len(dungeons), 0, deque()
    dp.append([k, []])
    while dp:
        p, v = dp.pop()
        print(p, v)
        for i in range(L):
            a, b = dungeons[i]
            if i not in v and p >= a:
                dp.append([p - b, v + [i]])
            else:
                n = max(n, len(v))
    print(n)
    return n


solution(80, [[80, 20], [50, 40], [30, 10]])
