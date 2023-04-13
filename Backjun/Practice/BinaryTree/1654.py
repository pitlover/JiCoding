'''
4 11
802
743
457
539
'''
'''
5 10
1
100
100
100
100
'''
'''
4 8
13
13
13
13
'''
import sys

n, k = map(int, input().split())

lines = []
max_line = 0

for i in range(n):
    line = int(sys.stdin.readline().rstrip())
    lines.append(line)
    if max_line < line:
        max_line = line

start, end = 1, max_line


def get_cnt(value):
    cnt = 0
    for line in lines:
        cnt += (line // value)
    return cnt


if get_cnt(max_line) == k:
    print(max_line)
    exit()
results = []
result = None
while start <= end:
    mid = (start + end) // 2
    cnt = get_cnt(mid)
    # print(f"range : {start}-{end} ({mid}), cnt : {cnt}")
    if cnt == k:
        result = mid
        results.append(mid)

    if cnt < k:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

# print(results)
if len(results) == 0:
    results.append(result)
print(max(results))
