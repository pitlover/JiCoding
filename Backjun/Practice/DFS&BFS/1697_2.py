'''
5 17
'''
# X -> (X-1, X+1, 2X)
from collections import deque  # BFS

n, k = map(int, input().split())
is_visited = [False] * 100001
queue = deque([(n, 0)])

while queue:
    node, stage = queue.popleft()
    if node == k:
        print(stage)
        break
    if 0 <= node <= 100000 and not is_visited[node]:
        is_visited[node] = True
        if node - 1 >= 0 and not is_visited[node - 1]:
            queue.append((node - 1, stage + 1))
        if node + 1 <= 100000 and not is_visited[node + 1]:
            queue.append((node + 1, stage + 1))
        if node * 2 <= 100000 and not is_visited[2 * node]:
            queue.append((node * 2, stage + 1))
