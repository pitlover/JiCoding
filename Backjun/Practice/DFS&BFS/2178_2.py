'''
4 6
101111
101010
101011
111011
'''
n, m = map(int, input().split())

mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]
matrix = []
for i in range(n):
    matrix.append(list(map(int, input())))
visited = [[False] * m for _ in range(n)]
count = [[0] * m for _ in range(n)]
from collections import deque

queue = deque()
queue.append([0, 0])

while queue:
    x, y = queue.popleft()

    if not visited[x][y]:
        visited[x][y] = True

        for i in range(4):
            nxt_x, nxt_y = x + mov[i][0], y + mov[i][1]

            if 0 <= nxt_x <= n - 1 and 0 <= nxt_y <= m - 1 and matrix[nxt_x][nxt_y] == 1:
                if not visited[nxt_x][nxt_y]:
                    count[nxt_x][nxt_y] = count[x][y] + 1
                    queue.append([nxt_x, nxt_y])
print(count[-1][-1]+1)
'''
# Backtracking -> Time error
def bfs(x, y, count, visited):
    global matrix
    if (x, y) == (n - 1, m - 1):
        print(count+1)
        exit()
        return

    for i in range(4):
        nxt_x, nxt_y = x + mov[i][0], y + mov[i][1]

        if 0 <= nxt_x <= n - 1 and 0 <= nxt_y <= m - 1 and matrix[nxt_x][nxt_y] == 1:
            if visited[nxt_x][nxt_y] == True:
                continue
            visited[nxt_x][nxt_y] = True
            bfs(nxt_x, nxt_y, count + 1, visited)
            visited[nxt_x][nxt_y] = False


matrix = []
for i in range(n):
    matrix.append(list(map(int, input())))
visited = [[False] * m for _ in range(n)]
bfs(0, 0, 0, visited)

'''
