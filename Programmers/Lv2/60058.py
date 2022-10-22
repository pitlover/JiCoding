# 괄호 변환
# Help but success

from collections import deque


def spec(u):
    if u == ")(":
        return ""

    u = u[1:-1]
    print("u = ", u)

    x = []
    for a in range(len(u)):
        if u[a] == "(":
            x.append(")")
        else:
            x.append("(")

    print("spec", str(x))

    return x


def split_2(p):
    u = []
    count = 0
    for a in range(len(p)):
        if p[a] == "(":
            count += 1
        else:
            count -= 1
        u.append(p[a])

        if count == 0:
            break

    return p[:len(u)], p[len(u):]


def is_corr(p):
    print("*********")

    queue = deque()
    p = list(p)
    if p[0] == ")":
        return False
    queue.append(p[0])
    count = 1

    while queue:
        for a in range(1, len(p)):
            print(queue, a, p[a])
            if p[a] == "(":
                queue.append(p[a])
                count += 1
            else:
                queue.pop()
                count -= 1

            if count < 0:
                print("count < 0")
                print("**** F *****")
                return False
            print(count)
        print("**** T *****")
        return True
    print("**** F *****")
    return False


def solution(p):
    if p == "":
        return p

    u, v = split_2(p)

    if is_corr(u):
        print("u = cor ", u)
        return u + str(solution(v))
    else:
        print("u = incor", u)
        return "(" + str(solution(v)) + ")" + "".join(spec(u))