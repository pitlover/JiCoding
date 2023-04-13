# ----- Sol 1 ------ #
'''
n, m = map(int, input().split())
from itertools import permutations

results = list(permutations(range(1, n + 1), m))

for a in results:
    print(*a)

'''

# Backtracking with DFS

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
