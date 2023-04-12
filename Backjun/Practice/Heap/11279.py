'''
13
0
1
2
0
0
3
2
1
0
0
0
0
0
'''
from heapq import heappop, heappush
import sys
n = int(input())
heap = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heappush(heap, -a)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-1 * heappop(heap))
