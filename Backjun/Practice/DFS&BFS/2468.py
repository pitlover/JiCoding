'''
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
'''
N = int(input())
matrix = [[] for _ in range(N)]
max_city = -1
for _ in range(N):
    matrix[_] = list(map(int, input().split()))
    max_city = max(max_city, max(matrix[_]))
mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]
from collections import deque


def check(rain):
    rain_matrix = [[0] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            rain_matrix[a][b] = max(0, matrix[a][b] - rain)
    visited = [[False] * N for _ in range(N)]

    tmp = 0

    queue = deque()
    for a in range(N):
        for b in range(N):
            if rain_matrix[a][b] != 0 and not visited[a][b]:
                tmp += 1
                queue.append([a, b])

                while queue:
                    x, y = queue.popleft()

                    if not visited[x][y]:
                        visited[x][y] = True
                        for i, j in mov:
                            nxt_x, nxt_y = x + i, y + j

                            if 0 <= nxt_x < N and 0 <= nxt_y < N and rain_matrix[nxt_x][nxt_y] != 0:
                                queue.append([nxt_x, nxt_y])

    return tmp


result = 0
for rain in range(0, max_city + 1):
    rain_result = check(rain)
    result = max(result, rain_result)
print(result)
