'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''
'''
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
'''
m, n = map(int, input().split())
matrix = []
# matrix = [list(map(int, input().split(" "))) for _ in range(n)]
is_visited = [[False] * m for _ in range(n)]
days = [[0] * m for _ in range(n)]

from collections import deque

queue = deque()
minus = 0
for i in range(n):
    inputs = list(map(int, input().split()))
    matrix.append(inputs)
    for j in range(m):
        if inputs[j] == 1:
            queue.append((i, j, 1))
        elif inputs[j] == -1:
            minus += 1

zeros = m*n - minus
mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while queue:
    x, y, c = queue.popleft()

    if not is_visited[x][y]:
        is_visited[x][y] = True
        zeros -= 1
        days[x][y] = c

        for ii, jj in mov:
            nxt_x, nxt_y = x + ii, y + jj
            if 0 <= nxt_x < n and 0 <= nxt_y < m and matrix[nxt_x][nxt_y] == 0 and not is_visited[nxt_x][nxt_y]:
                queue.append((nxt_x, nxt_y, c + 1))
                matrix[nxt_x][nxt_y] = 1
result = -1
if zeros != 0:
    print(-1)
else:
    for i in days:
        tmp = max(i)
        if result < tmp:
            result = tmp
    print(result-1)
