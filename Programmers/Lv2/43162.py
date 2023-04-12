from collections import deque


def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if not visited[i]:
            queue = deque()
            visited[i] = True
            answer += 1
            queue.append(i)

            while queue:
                node = queue.pop()
                for nxt, is_link in enumerate(computers[node]):
                    if is_link == 1 and not visited[nxt]:
                        visited[nxt] = True
                        queue.append(nxt)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
