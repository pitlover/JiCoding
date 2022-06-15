# 짝지어 제거하기
# Success

from collections import deque


def solution(s):
    s = list(s)
    queue = deque()
    queue.append(s[0])

    while queue:
        for a in range(1, len(s)):
            if len(queue) == 0:
                queue.append(s[a])
                continue

            if queue[-1] == s[a]:
                queue.pop()
            else:
                queue.append(s[a])
        break

    if len(queue) == 0:
        return 1
    else:
        return 0
