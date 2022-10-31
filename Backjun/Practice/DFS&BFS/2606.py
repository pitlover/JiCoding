'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
N = int(input())
n = int(input())
matrix = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(n):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)


from collections import deque
queue = deque()

queue.append(1)
result = 0
while queue:
    node = queue.pop()

    if not visited[node]:
        result += 1
        visited[node] = True
        for victim in matrix[node]:
            queue.append(victim)
print(result-1)