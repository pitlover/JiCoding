'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
'''
from collections import deque


def solution(N, location, priorities):
    dict_key = {chr(i + 65): priorities[i] for i in range(N)}
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
    return result.index(chr(location + 65)) + 1


cases = int(input())

for i in range(cases):
    N, location = map(int, input().split())
    priorities = list(map(int, input().split()))
    print(solution(N, location, priorities))
