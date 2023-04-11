'''
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
'''
from collections import deque
import sys
N = int(input())
queue = deque()


def command(string_command):
    if string_command[:4] == "push":
        queue.append(string_command.split(" ")[-1])
    elif string_command == "top":
        if len(queue) == 0:
            print(-1)
        else:
            a = queue.pop()
            print(a)
            queue.append(a)
    elif string_command == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif string_command == "size":
        print(len(queue))
    elif string_command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    return


for i in range(N):
    # command(input())
    a = sys.stdin.readline().rstrip()
    command(a)