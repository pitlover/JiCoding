'''
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
'''
M, N, K = map(int, input().split())
matrix = [[1] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for a in range(K):
    a_x, a_y, b_x, b_y = map(int, input().split())  # 0, 2, 4, 4
    start_x = M - b_y
    start_y = a_x
    for i in range(b_y - a_y):
        for j in range(b_x - a_x):
            matrix[start_x + i][start_y + j] = 0
 
from collections import deque

mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque()
size = []
for a in range(M):
    for b in range(N):
        if matrix[a][b] == 1 and not visited[a][b]:
            visited[a][b] = True
            result = 0
            queue.append([a, b])

            while queue:
                x, y = queue.pop()

                for i, j in mov:
                    nxt_x, nxt_y = x + i, y + j
                    if 0 <= nxt_x < M and 0 <= nxt_y < N and matrix[nxt_x][nxt_y] == 1 and not visited[nxt_x][nxt_y]:
                        matrix[nxt_x][nxt_y] = matrix[x][y] + 1
                        queue.append([nxt_x, nxt_y])
                        result += 1
            size.append(result+1)
print(len(size))
size.sort()
for a in size:
    print(a, end = " ")