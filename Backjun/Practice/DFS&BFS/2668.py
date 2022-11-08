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
# print(up, down)
matrix = [[] for _ in range(N + 1)]
for a in range(N):
    matrix[a + 1].append(down[a])
# print(matrix)

visited = [False] * (N + 1)
result_list = set()


def dfs(node, history):
    for i in matrix[node]:
        if i in history:
            global result
            result_list.add(i)
            return

        if not visited[i]:
            visited[i] = True
            history.append(node)
            dfs(i, history)
            history.remove(node)
            visited[i] = False


for a in range(1, N + 1):
    visited[a] = True
    dfs(a, [a])
    visited[a] = False
result_list = sorted(result_list)
print(len(result_list))

for _ in result_list:
    print(_)
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
