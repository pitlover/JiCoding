'''
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
'''
from collections import deque

n = int(input())


def check(text):
    text = list(text)
    queue = deque()
    for par in text:
        if par == "(":
            queue.append("(")
        else:
            if len(queue) == 0:
                return "NO"
            queue.pop()
    if len(queue) == 0:
        return "YES"
    else:
        return "NO"


for i in range(n):
    print(check(input()))
