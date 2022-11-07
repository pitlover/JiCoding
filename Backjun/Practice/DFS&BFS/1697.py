'''
5 17
'''
# 메모리 초과
N, K = map(int, input().split())
mov = [-1, 1, 2]

from collections import deque

queue = deque()
queue.append(N)

floor = [0] * 100001
floor[N] = 0

while queue:
    pos = queue.popleft()
    if pos == K:
        print(floor[K])
        exit()

    for a in mov:
        if a == 2:
            nxt_pos = pos * 2
        else:
            nxt_pos = pos + a
        if 0 <= nxt_pos <= 100000:
            if floor[nxt_pos] == 0:
                queue.append(nxt_pos)
                floor[nxt_pos] = floor[pos] + 1
