'''
2 4
CAAB
ADCB
'''

N, M = map(int, input().split())
matrix = [[] for _ in range(N)]

for a in range(N):
    matrix[a] = [*input()]

mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = 1
path = {matrix[0][0]: True}


def dfs(x, y, count):
    global result
    result = max(result, count)

    for i, j in mov:
        nxt_x, nxt_y = x + i, y + j
        if 0 <= nxt_x < N and 0 <= nxt_y < M and path.get(matrix[nxt_x][nxt_y], False) is False:
            path[matrix[nxt_x][nxt_y]] = True
            dfs(nxt_x, nxt_y, count + 1)
            path[matrix[nxt_x][nxt_y]] = False


dfs(0, 0, 1)

print(result)
'''
3 4
ABCD
BCDA
CDEF
'''
# def dfs(x, y, count):
#     global ans
#     ans = max(ans, count)
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
#             alphas.add(maps[nx][ny])
#             dfs(nx, ny, count+1)
#             alphas.remove(maps[nx][ny])
# alphas.add(maps[0][0])
# dfs(0, 0, 1)
# print(ans)
