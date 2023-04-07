'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
print(graph)
for _ in range(M):
    s, d = map(int, input().split())
    graph[s].append(d)
    graph[d].append(s)

print(graph)

from collections import deque

def BFS(graph):
    queue = deque()
    queue.append(V)

    while True:
        node = queue.pop()



BFS(graph)
DFS(graph)