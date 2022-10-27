'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''
from collections import deque


def dfs(matrix, N):
    result = 0
    mov = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[False] * N for _ in range(N)]
    # for a in matrix:
    #     print(a)
    # print("*" * 10)
    queue = deque()
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                result += 1
                queue.append([i, j])

                while queue:
                    x, y = queue.popleft()
                    if not visited[x][y]:
                        visited[i][j] = True
                        for a, b in mov:
                            nxt_x, nxt_y = x + a, y + b
                            if 0 <= nxt_x < N and 0 <= nxt_y < N and matrix[nxt_x][nxt_y] == 1 and not visited[nxt_x][nxt_y]:
                                # print(f"cur : {x},{y}, nxt : {nxt_x},{nxt_y}")
                                queue.append([nxt_x, nxt_y])
                                matrix[nxt_x][nxt_y] = matrix[x][y] + 1
                        # for a in matrix:
                        #     print(a)
                        # print("*" * 10)

    # print(result)
    return result


N = int(input())
matrix_R = [[0] * N for _ in range(N)]
matrix_G = [[0] * N for _ in range(N)]
matrix_B = [[0] * N for _ in range(N)]
matrix_RG = [[0] * N for _ in range(N)]

for a in range(N):
    color = list(input())
    for idx, col in enumerate(color):
        if col == "R":
            matrix_R[a][idx] = 1
            matrix_RG[a][idx] = 1
        elif col == "B":
            matrix_B[a][idx] = 1
        else:
            matrix_G[a][idx] = 1
            matrix_RG[a][idx] = 1

result_R = dfs(matrix_R, N)
result_G = dfs(matrix_G, N)
result_B = dfs(matrix_B, N)
result_RG = dfs(matrix_RG, N)
print(result_R+result_B+result_G)
print(result_RG+result_B)
