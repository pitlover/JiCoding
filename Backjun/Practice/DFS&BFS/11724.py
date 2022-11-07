'''
6 5
1 2
2 5
5 1
3 4
4 6
'''
N, M = map(int, input().split())
matrix = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)

from collections import deque

visited = [False] * (N + 1)
result = 0


def dfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.pop()

        if not visited[node]:
            visited[node] = True
            for b in matrix[node]:
                queue.append(b)


for a in range(1, N + 1):
    if not visited[a]:
        result += 1
        dfs(a)
print(result)
