'''
3
1 3
2 4
3 5
'''
n = int(input())
times = []
for i in range(n):
    start, end = map(int, input().split())
    times.append([start, end])

times.sort(key=lambda x: x[0])
print(times)
result = 0

import heapq

