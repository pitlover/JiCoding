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
from collections import deque

N = int(input())
matrix = [[] for _ in range(N)]
visited = [[False] * N for _ in range(N)]
for _ in range(N):
    matrix[_] = list(map(int, input()))

num_town = []
queue = deque()
mov = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for a in range(N):
    for b in range(N):
        if matrix[a][b] == 1:

            queue.append([a, b])
            num = 1
            while queue:
                i, j = queue.popleft()

                if not visited[i][j]:
                    visited[i][j] = True
                    for ii, jj in mov:
                        nxt_a, nxt_b = i + ii, j + jj
                        if 0 <= nxt_a < N and 0 <= nxt_b < N and matrix[nxt_a][nxt_b] == 1 and not visited[nxt_a][nxt_b]:
                            matrix[nxt_a][nxt_b] = matrix[i][j] + 1
                            queue.append([nxt_a, nxt_b])
                            num +=1
                            # num = max(num, matrix[nxt_a][nxt_b])
                # for _ in matrix:
                #     print(_)
                # print("*" * 10)
            num_town.append(num)
            # print(num)
# print(num_town)
print(len(num_town))
num_town.sort()
for a in num_town:
    print(a)