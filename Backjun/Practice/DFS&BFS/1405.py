'''
2 25 25 25 25
'''
n, E, W, S, N = map(int, input().split())
mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]
from collections import deque

queue = deque()
map = ["E", "W", "N", "S"]
result_path = []


def dfs(cur_pos, number, path_list, visit_pos):
    if cur_pos in visit_pos:
        result_path.append(path_list)
        return

    if number >= n:
        return

    visit_pos.append(cur_pos)

    for idx in range(4):
        nxt_pos_x, nxt_pos_y = cur_pos[0] + mov[idx][0], cur_pos[1] + mov[idx][1]
        dfs((nxt_pos_x, nxt_pos_y), number + 1, path_list + map[idx], visit_pos.copy())


dfs((0, 0), 0, "", [])

total_prob = 0
for a in result_path:
    prob = 1
    for b in a:
        if b == "E":
            c = E
        elif b == "W":
            c = W
        elif b == "S":
            c = S
        elif b == "N":
            c = N
        prob *= (0.01 * c)
    total_prob += prob
print(1 - total_prob)
