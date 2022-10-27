'''
4 6
101111
101010
101011
111011
'''
from collections import deque
def BFS(matrix, cost, x, y):
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.append([x, y])
    visited = [[False] * M for _ in range(N)]

    while queue:
        x, y = queue.popleft()

        if not visited[x][y]:
            for i, j in move:
                n_x, n_y = (x + i, y + j)

                if 0 > n_x or n_x >= N or 0 > n_y or n_y >= M:
                    continue

                if matrix[n_x][n_y] == '1':
                    matrix[n_x][n_y] = int(matrix[x][y]) + 1
                    queue.append([n_x, n_y])
                    visited[x][y] = True

    return matrix[-1][-1]


N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
cost = [[0] * M for _ in range(N)]

for _ in range(N):
    matrix[_] = (list(input()))

print(BFS(matrix, cost, 0, 0))
