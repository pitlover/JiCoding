# 프린터
# Little Help => Success

from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    index = deque(_ for _ in range(len(queue)))

    while queue:
        tmp = queue.popleft()
        if tmp == max(priorities):
            priorities.remove(tmp)
            answer += 1
            tmp_index = index.popleft()
            if tmp_index == location:
                return answer
        else:
            queue.append(tmp)
            index.append(index.popleft())

    return answer
