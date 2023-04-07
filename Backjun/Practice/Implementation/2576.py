'''
12
77
38
41
53
92
85
'''
import sys
nums = []
sum_results = 0
min_results = sys.maxsize

for _ in range(7):
    x = int(input())
    if x % 2 == 1:
        sum_results += x
        min_results = min(x, min_results)
if min_results == sys.maxsize:
    print(-1)
else:
    print(sum_results)
    print(min_results)