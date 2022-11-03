'''
5 4
0 1
1 2
2 3
3 4
'''
# CHECK !!
N, M = map(int, input().split())
matrix = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

# for _ in matrix:
#     print(_)
# print("*" * 10)

def dfs(node, number):
    if number == 4:
        print(1)
        exit()

    for b in matrix[node]:
        if not visited[b]:
            visited[b] = True
            dfs(b, number + 1)
            visited[b] = False

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
print(0)
