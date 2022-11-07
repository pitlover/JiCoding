'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''
N = int(input())
matrix = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)
parent = [-1] * (N + 1)

visited = [False] * (N + 1)
from collections import deque

queue = deque()
queue.append(1)

while queue:
    node = queue.popleft()  # [1, 4]

    if not visited[node]:
        visited[node] = True

        for a in matrix[node]:
            queue.append(a)
            if parent[a] == -1 and not visited[a]:
                parent[a] = node
for a in parent[2:]:
    print(a)