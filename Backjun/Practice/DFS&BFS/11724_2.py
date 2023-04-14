'''
6 5
1 2
2 5
5 1
3 4
4 6
'''
from collections import deque

n, m = map(int, input().split())

matrix = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

count = 0
is_visited = [0] * (n + 1)

for a in range(1, n + 1):
    if is_visited[a] == 0:
        count += 1

        queue = deque()
        queue.append(a)

        while queue:
            node = queue.popleft()

            if is_visited[node] == 0:
                is_visited[node] = 1
                for nxt_node in matrix[node]:
                    if is_visited[nxt_node] == 0:
                        queue.append(nxt_node)
print(count)
