'''
8
'''
# (0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596)
result = 0


def is_update(arr, i):
    # i : (len(arr), i), arr : (idx, loc)
    # for idx, loc in enumerate(arr):
    #     if loc == i or (abs(len(arr) - idx) == abs(i - loc)):
    #         return False
    #
    for idx in range(len(arr)):
        if arr[idx] == i or (abs(len(arr) - idx) == abs(i - arr[idx])):
            return False
    return True


def dfs(arr):
    global result
    if len(arr) == n:
        result += 1
        return

    for i in range(n):
        if is_update(arr, i):
            arr.append(i)
            dfs(arr)
            arr.pop()


from sys import stdin

n = int(stdin.readline())
if n == 1:
    print(1)
    exit()
dfs([])
print(result)
