'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''

M, N = map(int, input().split())
matrix = [[] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
minus = 0

from collections import deque

queue = deque()

for a in range(N):
    matrix[a] = list(map(int, input().split()))
    for idx, b in enumerate(matrix[a]):
        if b == -1:
            minus += 1
        elif b == 1:
            queue.append([a, idx])
if minus + len(queue) == N * M:
    print(0)
    exit()
# bfs
tomato = 0
mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]
day = -1
while queue:
    x, y = queue.popleft()

    if visited[x][y] == False:
        visited[x][y] = True
        tomato += 1
        for i, j in mov:
            nxt_x, nxt_y = x + i, y + j
            if 0 <= nxt_x < N and 0 <= nxt_y < M and matrix[nxt_x][nxt_y] != -1 and matrix[nxt_x][nxt_y] == False:
                matrix[nxt_x][nxt_y] = matrix[x][y] + 1
                queue.append([nxt_x, nxt_y])
                day = max(day, matrix[x][y])

        if N * M == tomato + minus:
            print(day)
            exit()
print(-1)
