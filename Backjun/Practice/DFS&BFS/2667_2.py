'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
is_visited = [[False] * n for _ in range(n)]
nums_list = [[0] * n for _ in range(n)]
result = []

from collections import deque

mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for x in range(n):
    for y in range(n):
        if not is_visited[x][y] and matrix[x][y] == 1:
            queue = deque()
            queue.append((x, y))
            max_tmp = 0

            while queue:
                a, b = queue.pop()

                if not is_visited[a][b]:
                    is_visited[a][b] = True
                    max_tmp += 1

                    for ii, jj in mov:
                        nxt_x, nxt_y = a + ii, b + jj
                        if 0 <= nxt_x < n and 0 <= nxt_y < n and matrix[nxt_x][nxt_y] == 1 and not is_visited[nxt_x][
                            nxt_y]:
                            queue.append((nxt_x, nxt_y))
            result.append(max_tmp)

print(len(result))
result.sort()
for a in result:
    print(a)