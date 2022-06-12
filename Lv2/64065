# 튜플
# Success

def solution(s):
    s = s[2:-2].split("},{")
    s = sorted(s, key = lambda x: len(x))
    tmp = set()
    result = []
    for a in s:
        a = set(map(int, a.split(",")))
        next = a.difference(tmp)
        tmp = tmp.union(next)
        next = list(next)
        result.append(next[0])
    return result
