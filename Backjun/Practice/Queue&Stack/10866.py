'''
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
'''

from collections import deque
import sys
N = int(input())
queue = deque()


def command(string_command):
    if string_command[:9] == "push_back":
        num = string_command.split(" ")[-1]
        queue.append(num)
    elif string_command[:10] == "push_front":
        num = string_command.split(" ")[-1]
        queue.appendleft(num)
    elif string_command == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif string_command == "pop_back":
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
    elif string_command == "front":
        if len(queue) == 0:
            print(-1)
        else:
            a = queue.popleft()
            print(a)
            queue.appendleft(a)
    elif string_command == "back":
        if len(queue) == 0:
            print(-1)
        else:
            a = queue.pop()
            print(a)
            queue.append(a)

    return


for i in range(N):
    command(sys.stdin.readline().rstrip())
