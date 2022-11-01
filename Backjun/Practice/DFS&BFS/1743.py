'''
3 4 5
3 2
2 2
3 1
2 3
1 1
'''
N, M, K = map(int, input().split())
matrix = [["."] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for a in range(K):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = '#'

from collections import deque

queue = deque()
mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = -1
for a in range(N):
    for b in range(M):
        if matrix[a][b] == '#' and not visited[a][b]:

            queue.append([a, b])
            visited[a][b] = True
            cur = 1

            while queue:
                x, y = queue.pop()

                for i, j in mov:
                    nxt_x, nxt_y = x + i, y + j
                    if 0 <= nxt_x < N and 0 <= nxt_y < M and matrix[nxt_x][nxt_y] == "#" and not visited[nxt_x][nxt_y]:
                        queue.append([nxt_x, nxt_y])
                        visited[nxt_x][nxt_y] = True
                        cur += 1
                result = max(result, cur)

print(result)