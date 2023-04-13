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
import sys

n, k = map(int, input().split())

lines = []
max_line = 0
for i in range(n):
    line = int(sys.stdin.readline())
    lines.append(line)
    if max_line < line:
        max_line = line

lines.sort()


def get_n(cut):
    count = 0
    for line in lines:
        count += (line // cut)

    return count


def binarysearch(result, low, high):
    mid = (low + high) // 2
    tmp_k = get_n(mid)

    # print(f"range : {low}-{high}, mid :{mid}, cut : {tmp_k}, result : {result}")

    if tmp_k == k:
        print(mid)
        return
    else:
        result = mid

    if low >= high:
        print(result)
        return

    if tmp_k < k:
        binarysearch(result, low, mid - 1)
    else:
        binarysearch(result, mid + 1, high)


if get_n(max_line) == k:
    print(max_line)
else:
    binarysearch(None, 1, max_line)
