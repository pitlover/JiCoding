'''
4 7
20 15 10 17
'''
'''
4 2
10 10 10 10
'''
import sys
n, m = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for tree in trees:
        if tree > mid:
            cnt += tree-mid
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
