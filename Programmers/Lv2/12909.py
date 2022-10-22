# 올바른 괄호
# Runtime error => Success
def solution(s):
    cur = 0
    for data in s:
        if data == "(":
            cur += 1
        else:
            cur -= 1
        if cur < 0:
            return False

    if cur == 0:
        return True
    else:
        return False


## 런타임 에러 아오...
'''
from collections import deque

def solution(s):
    queue = deque()
    if s[0] == ")":
        return False

    queue.append("(")
    count = 1

    for data in range(1, len(s)):
        if s[data] == "(":
            queue.append(s[data])
        else:
            queue.pop()

        if len(queue) < 0:
            return False

    if len(queue) == 0:
        return True
    else:
        return False
'''
