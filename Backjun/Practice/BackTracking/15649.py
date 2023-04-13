# ----- Sol 1 ------ #
'''
n, m = map(int, input().split())
from itertools import permutations

results = list(permutations(range(1, n + 1), m))

for a in results:
    print(*a)

'''

# Backtracking with DFS
'''
n, m = map(int, input().split())

s = []
visited = [False] * (n + 1)


def dfs():
    global s

    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False


dfs()

'''
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]


def dfs(results):
    if len(results) == m:
        print(*results)
        return

    for i in arr:
        if i not in results:
            results.append(i)
            dfs(results)
            results.pop()


dfs([])
