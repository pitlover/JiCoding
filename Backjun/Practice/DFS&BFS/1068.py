'''
6
-1 0 1 5 5 0
1
'''
N = int(input())
nodes = list(map(int, input().split()))
del_node = int(input())
matrix = [[] for _ in range(N)]
visited = [False] * N
parent = [[] for _ in range(N)]
root = []
for a in range(N):
    if nodes[a] == -1:
        root.append(a)
    else:
        matrix[a].append(nodes[a])
        matrix[nodes[a]].append(a)
        parent[nodes[a]].append(a)

# print("before", matrix)

# del node
for a in matrix[del_node]:
    matrix[a].remove(del_node)
matrix[del_node] = []
# print("after", matrix)
# print("parent", parent)

for _ in range(N):
    if del_node in parent[_]:
        parent[_].remove(del_node)

result = 0
leaf = set()

for root_ in root:
    if root_ == del_node:
        root.remove(root_)

for root_ in root:
    if matrix[root_] == []:
        leaf.add(root_)
        root.remove(root_)


def dfs(node, number):
    if parent[node] == []: # leaf 인지 확인하는 조건이 틀린 듯
        global leaf
        leaf.add(node)
        # print("leaf", node)
        return 1

    for a in matrix[node]:
        if not visited[a]:
            visited[a] = True
            dfs(a, number + 1)
            visited[a] = False


for root_ in root:
    dfs(root_, 0)
    # print(len(leaf))
    # print("*"*10)
print(len(leaf))
