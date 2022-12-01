'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
'''
import sys
sys.setrecursionlimit(10 ** 4)
n = int(input())
tree = [[] for _ in range(n + 1)]
cost_dict = {}

for _ in range(n - 1):
    par, child, cost = map(int, input().split())
    cost_dict[f"{par}_{child}"] = cost
    cost_dict[f"{child}_{par}"] = cost
    tree[par].append(child)
    tree[child].append(par)

visited = [-1 for _ in range(n+1)]

def dfs(node):
    for nxt in tree[node]:
        if visited[nxt] == -1:
            visited[nxt] = visited[node] + cost_dict[f"{node}_{nxt}"]
            dfs(nxt)

visited[1] = 0
dfs(1)

target = visited.index(max(visited))
visited = [-1 for _ in range(n+1)]
visited[target] = 0
dfs(target)
print(max(visited))


# 시간초과...ㅠㅠ 답은 다 받는 듯 하다...
# import sys
#
# sys.setrecursionlimit(10 ** 4)
#
# n = int(input())
# tree = [[] for _ in range(n + 1)]
# cost_dict = {}
#
# for _ in range(n - 1):
#     par, child, cost = map(int, input().split())
#     cost_dict[f"{par}_{child}"] = cost
#     cost_dict[f"{child}_{par}"] = cost
#     tree[par].append(child)
#     tree[child].append(par)
#
# leaf = []
# for _ in range(1, n + 1):
#     if len(tree[_]) == 1:
#         leaf.append(_)
#
#
# def dfs(src, number):
#     global path, result
#     result = max(result, number)
#
#     if len(tree[src]) > 0:
#         for des in tree[src]:
#             if des not in path:
#                 path.add(des)
#                 dfs(des, number + cost_dict[f"{src}_{des}"])
#                 path.remove(des)
#
# result = 0
#
# for src in leaf:  # dfs(src, des, number)
#     path = set()
#     path.add(src)
#     dfs(src, 0)
#
# print(result)
