'''
9 5 2
1 3
4 3
5 4
5 6
6 7
2 3
9 6
6 8
4
8
'''
N, R, U = map(int, input().split())

matrix = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

# get matrix of parent
from collections import deque

def dfs(matrix, root):
    queue = deque()
    queue.append(root)
    mini_visited = [False] * (N+1)
    result = 0
    print("dfs")
    while queue:
        node = queue.popleft()
        if not mini_visited[node]:
            mini_visited[node] = True
            result += 1
            for a in matrix[node]:
                queue.append(a)
    return result


def solution(root, matrix):
    if root == R:
        return N
    queue = deque()
    queue.append(R)
    flag = 0
    while queue:
        if flag == 1:
            break
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            for child in matrix[node]:
                if child == root:
                    flag = 1
                    print(dfs(matrix, root))
                    break
                else:
                    queue.append(child)

for _ in range(U):
    root = int(input())
    solution(root, matrix)
    exit()
'''
import sys
sys.setrecursionlimit(10**6)

n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

def dfs(x):
    dp[x] = 1
    for next in graph[x]:
        if not dp[next]:
            dfs(next)
            dp[x] += dp[next]

for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(r)

for _ in range(q):
    print(dp[int(sys.stdin.readline())])
    '''
