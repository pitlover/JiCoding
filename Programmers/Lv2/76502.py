# 괄호 회전하기
# Success

from collections import deque


def is_corr(s):
    s = list(s)
    queue = deque()
    a, b, c = 0, 0, 0  # (, {, [
    before = ""
    for txt in s:
        if txt in ["(", ")"]:
            if txt == "(":
                a += 1
                queue.append(txt)
            else:
                a -= 1
                if a < 0:
                    return False
                before = queue.pop()
                if before != "(":
                    return False
        elif txt in ["{", "}"]:
            if txt == "{":
                b += 1
                queue.append(txt)
            else:
                b -= 1
                if b < 0:
                    return False
                before = queue.pop()
                if before != "{":
                    return False
        elif txt == "[":
            c += 1
            queue.append(txt)
        else:
            c -= 1
            if c < 0:
                return False
            before = queue.pop()
            if before != "[":
                return False

    if a == 0 and b == 0 and c == 0:
        return True
    else:
        return False


def solution(s):
    answer = 0
    queue = deque(s)
    count, answer = 0, 0
    while queue and count < len(s):
        count += 1
        if is_corr(queue):
            answer += 1
        queue.append(queue.popleft())

    return answer


solution("[(])")
