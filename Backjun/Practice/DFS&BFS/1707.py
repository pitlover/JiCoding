'''
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
'''
# assign node with bfs -> 0, 1,...
# check whether adjacency node is different or not
# 이분 그래프 => 한 번 NO면 영원히 NO

# ******** #
# 한 정점에서 탐색을 시작했더니 답이 NO로 판명났으면, 그 답을 다시 YES로 바꿀 일은 절대로 없습니다.
# 예를 들어 1번 정점에서 탐색했더니 이분 그래프를 못 만들었다면, 4번 정점에서 탐색했더니 만들 수 있었다고 해도 답이 YES가 되지는 않습니다.
from collections import deque
from sys import *

n = int(stdin.readline())


def bfs(node, V, tree, edges):
    queue = deque()
    mark = [-1 for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]

    queue.append(node)
    for i in range(1, V + 1):
        if not visited[i]:
            queue.append(i)
            while queue:
                nnode = queue.popleft()

                if not visited[nnode]:
                    visited[node] = True
                    for nxt in tree[nnode]:
                        if mark[nxt] == -1:
                            mark[nxt] = (mark[nnode] + 1) % 2
                            queue.append(nxt)

    mark[node] = 1
    # step 2 : check
    flag = 0
    for a, b in edges:
        if mark[a] == mark[b] and mark[a] != -1:
            flag = -1
            break
    if flag == -1:
        return "NO"
    return "YES"


def sol():
    V, E = map(int, stdin.readline().split())
    tree = [[] for _ in range(V + 1)]
    edges = []
    for a in range(E):
        src, des = map(int, stdin.readline().split())
        tree[src].append(des)
        tree[des].append(src)
        edges.append([src, des])

    # step 1
    if bfs(1, V, tree, edges) == "NO":
        return "NO"
    return "YES"


result = []
for _ in range(n):
    result.append(sol())

for j in result:
    print(j)
