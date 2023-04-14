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
T = int(input())
from collections import deque

mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(matrix, is_visited):
    count = 0
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            if not is_visited[a][b] and matrix[a][b] == 1:
                count += 1
                queue = deque()
                queue.append((a, b))

                while queue:
                    x, y = queue.popleft()

                    if not is_visited[x][y]:
                        is_visited[x][y] = True
                        for i in range(4):
                            nxt_x, nxt_y = x + mov[i][0], y + mov[i][1]
                            if 0 <= nxt_x < m and 0 <= nxt_y < n and not is_visited[nxt_x][nxt_y] and matrix[nxt_x][
                                nxt_y] == 1:
                                queue.append((nxt_x, nxt_y))

    return count


for i in range(T):
    n, m, j = map(int, input().split())
    matrix = [[0] * n for _ in range(m)]
    is_visited = [[False] * n for _ in range(m)]
    for ii in range(j):
        a, b = map(int, input().split())
        matrix[b][a] = 1
    print(bfs(matrix, is_visited))
