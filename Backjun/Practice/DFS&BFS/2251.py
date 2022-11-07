'''
8 9 10
'''

A, B, C = map(int, input().split())

from collections import deque

queue = deque()
queue.append([0, 0])  # queue(a, b) : x = a, y = b, z = c-(a+b)
visited = [[False] * 201 for _ in range(201)]

result = set()

# 완전탐색 -> bfs -> 모든 경우의 수 다 구해서 -> A=0일때만 저장

while queue:
    a, b = queue.popleft()
    c = C - (a + b)

    if a == 0:
        result.add(c)

    if not visited[a][b]:
        visited[a][b] = True

        # 물 옮기는 경우의 수 다시 하기
        # A->B
        water = min(a, B - b)
        queue.append([a - water, b + water])
        # A->C
        water = min(a, C - c)
        queue.append([a - water, b])
        # queue.append([a - water, c + water])
        # B->A
        water = min(b, A - a)
        queue.append([a + water, b - water])
        # queue.append([b - water, a + water])
        # B->C
        water = min(b, C - c)
        queue.append([a, b - water])
        # queue.append([b - water, c + water])
        # C->A
        water = min(c, A - a)
        queue.append([a + water, b])
        # queue.append([c - water, a + water])
        # C->B
        water = min(c, B - b)
        queue.append([a, b + water])
        # queue.append([c - water, b + water])

result = sorted(result)
for a in result:
    print(a, end=" ")
