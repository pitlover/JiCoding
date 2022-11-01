'''
5 5
#####
#..B#
#.#.#
#RO.#
#####
'''
N, M = map(int, input().split())
matrix = [[] * M for _ in range(N)]

from collections import deque

queue = deque()
path = {}
for a in range(N):
    matrix[a] = list(input())
    for b in range(M):
        if matrix[a][b] == "R":
            queue.append([a, b])
            path[f"{a}_{b}"] = 0
            name = f"{a}_{b}"
        elif matrix[a][b] == "B":
            b_x, b_y = a, b
print(matrix)
mov = [(-1, 0), (1, 0), (0, -1), (0, 1)]
'''
1. B가 구멍에 안 빠지면, R&B 움직이기
2. O 확인, 토탈 시도 10인지 확인
'''
def gravity(matrix, mov_i, mov_j, x, y, stage: str = "R"):
    while matrix[x][y] != "#":
        x += mov_i
        y += mov_j
        if stage == "B" and matrix[x][y] == "O":
            return -1, -1
        if stage == "R" and matrix[x][y] == "O":
            return "Success", "Success"

    return x - mov_i, y - mov_j


def move(matrix, mov_i, mov_j, r_x, r_y, b_x, b_y):
    '''
    A 먼저 구하고 -> B 구하기
    '''
    nxt_b_x, nxt_b_y = gravity(matrix, mov_i, mov_j, b_x, b_y, stage="B")
    if nxt_b_x == -1:
        return -1, -1
    nxt_r_x, nxt_r_y = gravity(matrix, mov_i, mov_j, r_x, r_y)
    print(mov_i, mov_j, ":", nxt_r_x, nxt_r_y, nxt_b_x, nxt_b_y)
    print("-----")

    return nxt_r_x, nxt_r_y, nxt_b_x, nxt_b_y


trial = 0

while queue:
    r_x, r_y = queue.pop()  # position of A -> DFS
    path[name + f":{r_x}_{r_y}"] = path[name] + 1
    name = name + f":{r_x}_{r_y}"

    for mov_i, mov_j in mov:
        result = move(matrix, mov_i, mov_j, r_x, r_y, b_x, b_y)
        if result[0] == -1:
            trial = 0
            continue
        elif result[0] == "Success":
            if path[name] <= 10:
                print(path[name])
                exit()
        else:
            b_x, b_y = result[-2], result[-1]  # B 구슬 위치
            queue.append([result[0], result[1]])
        print(f"queue : {queue}")

print(-1)