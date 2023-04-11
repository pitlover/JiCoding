# 프린터
# Little Help => Success

from collections import deque


def solution(priorities, location):
    dict_key = {chr(i + 65): priorities[i] for i in range(len(priorities))}
    queue = deque(dict_key.items())

    result = []
    priorities.sort(reverse=True)
    max_prior = priorities[0]

    while queue:
        ch, prior = queue.popleft()
        if prior == max_prior:
            result.append(ch)
            priorities.remove(prior)
            if len(priorities) > 0:
                max_prior = priorities[0]
        else:
            queue.append((ch, prior))
    return result.index(chr(location+65)) + 1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
