'''
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
'''
'''
1
4
0 0
3 3
'''
n = int(input())

from collections import deque

mov = [(-2, 1), (-1, 2), (-2, -1), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2)]


def dfs(x, y, s):
    visited = [[False] * s for _ in range(s)]
    result = 999999999

    queue = deque()
    queue.append((x, y, 0))

    while queue:
        x, y, cnt = queue.popleft()
        if (x, y) == (d_x, d_y):
            result = min(result, cnt)

        if not visited[x][y]:
            visited[x][y] = True

            for i, j in mov:
                nxt_x, nxt_y = x + i, y + j
                if 0 <= nxt_x < s and 0 <= nxt_y < s and not visited[nxt_x][nxt_y]:
                    queue.append((nxt_x, nxt_y, cnt + 1))
    return result


for i in range(n):
    s = int(input())
    s_x, s_y = map(int, input().split())
    d_x, d_y = map(int, input().split())

    print(dfs(s_x, s_y, s))
