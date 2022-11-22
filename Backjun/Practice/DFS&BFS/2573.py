'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''

N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
for _ in range(N):
    matrix[_] = list(map(int, input().split()))

from collections import deque
from copy import deepcopy

mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def melting():
    moun = 0
    global matrix
    matrix_ = deepcopy(matrix)
    for a in range(N):
        for b in range(M):
            if matrix[a][b] > 0:
                moun += 1
                melt = 0
                for i, j in mov:
                    nxt_x, nxt_y = a + i, b + j
                    if 0 <= nxt_x < N and 0 <= nxt_y < M and matrix[nxt_x][nxt_y] == 0:
                        melt += 1
                    matrix_[a][b] = max(0, matrix[a][b] - melt)
    # for a in matrix_:
    #     print(a)
    # print("*" * 10)
    if moun == 0:
        return -1

    # check matrix_
    visited = [[False] * M for _ in range(N)]

    check = 0
    for a in range(N):
        for b in range(M):
            if not visited[a][b] and matrix_[a][b] > 0:
                check += 1
                queue = deque()
                queue.append([a, b])
                while queue:
                    x, y = queue.popleft()
                    if not visited[x][y]:
                        visited[x][y] = True
                        for i, j in mov:
                            nxt_x, nxt_y = x + i, y + j
                            if 0 <= nxt_x < N and 0 <= nxt_y < M and matrix_[nxt_x][nxt_y] > 0 and not visited[nxt_x][nxt_y]:
                                queue.append([nxt_x, nxt_y])
    matrix = matrix_

    return check


result = 0
while True:
    a = melting()
    if a == -1:
        print(0)
        break
    elif a >= 2:
        print(result+1)
        break
    result += 1
