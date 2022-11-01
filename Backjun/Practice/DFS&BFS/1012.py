'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''
from collections import deque


def solution(M, N, baechu):
    matrix = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    mov = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for a in range(baechu):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    result = 0
    queue = deque()
    for a in range(N):
        for b in range(M):
            if matrix[a][b] == 1 and not visited[a][b]:
                result += 1
                queue.append([a, b])
                visited[a][b] = True

                while queue:
                    x, y = queue.pop()

                    for i, j in mov:
                        nxt_x, nxt_y = x + i, y + j
                        if 0 <= nxt_x < N and 0 <= nxt_y < M and matrix[nxt_x][nxt_y] == 1 and not visited[nxt_x][nxt_y]:
                            visited[nxt_x][nxt_y] = True
                            matrix[nxt_x][nxt_y] = 2
                            queue.append([nxt_x, nxt_y])
    print(result)
    return result


task = int(input())
for i in range(task):
    M, N, baechu = map(int, input().split())
    solution(M, N, baechu)
