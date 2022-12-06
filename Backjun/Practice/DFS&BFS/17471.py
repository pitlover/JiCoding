'''
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2
'''
n = int(input())
num = list(map(int, input().split()))
total = sum(num)
num.insert(0, 0)

matrix = [[] for _ in range(n + 1)]

for a in range(1, n + 1):
    input_ = input().split()
    for b in input_[1:]:
        matrix[a].append(int(b))

if n + (len(matrix[1]) + len(matrix[2])) == 2:
    print(abs(num[1] - num[2]))
    exit()
result = 10 ** 7

from collections import deque


def bfs(chk1):
    global matrix
    global num

    num_visited = 0
    tmp_result = 0

    queue = deque()
    visited = [False] * (n+1)
    queue.append(chk1[0])

    while queue:
        node = queue.popleft()


        if not visited[node]:
            visited[node] = True
            num_visited += 1
            tmp_result += num[node]
            for nxt_node in matrix[node]:
                if nxt_node in chk1 and not visited[nxt_node]:
                    queue.append(nxt_node)

    return num_visited, tmp_result

from itertools import combinations

for i in range(1, (n + 1)//2 + 1):
    check1 = list(combinations(range(1, n + 1), i))
    for chk1 in check1:
        chk2 = list(a for a in range(1, n + 1) if a not in chk1)

        if len(chk1) > 0 and len(chk2) > 0 :
            node_chk1, res_chk1 = bfs(chk1)
            node_chk2, res_chk2 = bfs(chk2)
            if node_chk1 + node_chk2 == n:
                result = min(result, abs(res_chk1 - res_chk2))
if result == 10 ** 7:
    result = -1
print(result)
# 1차 시
# def check(visited, tmp_result):
#     # check if remains node is connected or not
#
#     check_nodes = [n + 1 for n, a in enumerate(visited[1:]) if a == False]
#
#     if len(check_nodes) == 0:
#         return -1
#     visited_nodes = [n + 1 for n, a in enumerate(visited[1:]) if a == True]
#     check_visit = {}
#     for a in check_nodes:
#         check_visit[a] = 1
#     for a in visited_nodes:
#         check_visit[a] = 0
#     queue = deque()
#     queue.append(check_nodes[0])
#     while queue:
#         node = queue.popleft()
#         if check_visit[node] == 1:
#             check_visit[node] = 0
#             for nxt in matrix[node]:
#                 if check_visit[nxt] == 1:
#                     queue.append(nxt)
#     if sum(check_visit.values()) == 0:
#         return abs((total - tmp_result) - tmp_result)
#     else:
#         return -1
#
#
# def sol(src):
#     global result
#     visited = [False] * (n + 1)
#     queue = deque()
#     queue.append(src)
#
#     tmp_result = 0
#     # bfs
#     while queue:
#         node = queue.popleft()
#         if not visited[node]:
#             visited[node] = True
#             tmp_result += num[node]
#
#             for nxt in matrix[node]:
#                 queue.append(nxt)
#                 flag = check(visited, tmp_result)
#                 if flag != -1:
#                     result = min(result, flag)
#
#
# for chk in range(1, n + 1):
#     sol(chk)
#
# if result == 10 ** 7:
#     result = -1
# print(result)
