'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
coms = int(input())
n = int(input())
matrix = [[] for _ in range(coms + 1)]

for i in range(n):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

from collections import deque

queue = deque([1])
answer = 0
is_visited = [False] * (coms + 1)

while queue:
    node = queue.pop()
    if not is_visited[node]:
        answer += 1
        is_visited[node] = True
        for i in matrix[node]:
            if not is_visited[i]:
                queue.append(i)
print(answer-1)
