'''
7
3
1
1
5
5
4
6
'''
N = int(input())
up = [_ for _ in range(1, N + 1)]
down = []
for _ in range(N):
    down.append(int(input()))
print(up, down)
matrix = [[] for _ in range(N + 1)]
for a in range(N):
    matrix[a + 1].append(down[a])
print(matrix)


def dfs(node, link):
    if not visited[node]:
        visited[node] = True
        if link != [] and node in link:
            return "hello"

        for a in matrix[node]:
            link.append(a)
            dfs(a, link)


for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, [])

## 맞는데 시간초과 걸림... ㅠㅠ -> 완전탐색이 아닌 듯..
'''
N = int(input())
up = [_ for _ in range(1, N + 1)]
down = []
for _ in range(N):
    down.append(int(input()))

result = -1
for a in range(1, 1 << N):
    bit_list = []
    for b in range(N):
        if a & (1 << b):
            bit_list.append(b)

    tmp_up = set()
    tmp_down = set()
    for c in bit_list:
        tmp_up.add(up[c])
        tmp_down.add(down[c])

    if tmp_up == tmp_down:
        result = max(result, len(tmp_up))
        result_list = tmp_up
        break
print(result)
result_list = sorted(result_list)
for _ in result_list:
    print(_)
'''
