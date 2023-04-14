'''
2 25 25 25 25
'''

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, pos, count):
    global result
    if len(pos) == N + 1:
        result += count
        return

    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if (nx, ny) not in pos:
            pos.append((nx, ny))
            dfs(nx, ny, pos, count * (probs[i] / 100))
            pos.pop()


N, *probs = map(int, input().split())
result = 0

dfs(0, 0, [(0, 0)], 1)
print(result)
