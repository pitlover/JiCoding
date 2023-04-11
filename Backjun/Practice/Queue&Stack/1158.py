'''
7 3
'''

from collections import deque

n, k = map(int, input().split())
result = []
queue = deque()
queue2 = deque()
for i in range(n):
    queue.append(i + 1) # 1, 2, 3, 4, 5, 6, 7
count = 0
while queue:
    item = queue.popleft()
    count += 1

    if count == k:
        result.append(item)
        count = 0
    else:
        queue.append(item)

print(f'<{", ".join(map(str, result))}>')

