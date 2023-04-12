'''
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
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

for i in range(n):
    a = int(sys.stdin.readline())

    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            b, c = heappop(heap)
            print(c)
    else:
        heappush(heap, (abs(a), a))
