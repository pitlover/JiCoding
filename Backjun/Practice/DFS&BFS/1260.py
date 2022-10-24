'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
from collections import deque


def DFS(graph: list, V: int) -> list:
    queue = deque()
    visited = [False] * (N + 1)
    queue.append(V)
    route = []

    while queue:
        node = queue.pop()

        if not visited[node]:
            visited[node] = True
            route.append(node)
            graph[node].sort(reverse=True)
            for a in graph[node]:
                queue.append(a)

    return route


def BFS(graph: list, V: int) -> list:
    queue = deque()
    visited = [False] * (N + 1)
    queue.append(V)
    route = []
    while queue:
        node = queue.popleft()

        if not visited[node]:
            visited[node] = True
            route.append(node)
            graph[node].sort()
            for a in graph[node]:
                queue.append(a)

    return route


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for a in DFS(graph, V):
    print(a, end=" ")
print()
for a in BFS(graph, V):
    print(a, end=" ")
